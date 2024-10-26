# Load the saved model with custom objects
model = keras.models.load_model('captcha_model.keras', 
                              custom_objects={
                                  'CTCLayer': CTCLayer,
                                  'ctc_batch_cost': ctc_batch_cost
                              })

# Create prediction model
prediction_model = keras.models.Model(
    model.input[0], model.get_layer(name="dense2").output
)

# Rest of the interface code remains the same
def preprocess_image(image):
    if len(image.shape) == 3:
        image = Image.fromarray(image).convert('L')
        image = np.array(image)
    
    image = Image.fromarray(image).resize((img_width, img_height))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=-1)
    image = np.transpose(image, axes=[1, 0, 2])
    image = np.expand_dims(image, axis=0)
    
    return image

def predict_captcha(image):
    if image is None:
        return "Please upload an image"
    
    try:
        processed_image = preprocess_image(image)
        preds = prediction_model.predict(processed_image)
        pred_texts = decode_batch_predictions(preds)
        return pred_texts[0]
    except Exception as e:
         return f"Error processing image: {str(e)}"

# Create and launch the interface
interface = gr.Interface(
    fn=predict_captcha,
    inputs=gr.Image(type="numpy", label="Upload Captcha Image"),
    outputs=gr.Textbox(label="Predicted Text"),
    title="Captcha Recognition System",
    description="Upload a captcha image to get the predicted text.",
    examples=[
        ["sample_captcha.png"]
    ],
    cache_examples=True
)

# Launch the interface
interface.launch(share=True, debug=True)