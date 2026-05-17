import cv2
def main():
    image_path = 'saturn.jpg'
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error!Unable to load image at {image_path}")
        return
    print("Original image loaded successfully.")
    size={'small':(200, 200),'medium':(400, 400),'large':(600, 600)}
    for size_name,dimensions in size.items():
        resized=cv2.resize(image,dimensions)
        cv2.imshow(f"{size_name.capitalize()} Image", resized)
        cv2.imwrite(f"input_image_{size_name}.jpg", resized)
        print(f"Image resized to {dimensions[0]}x{dimensions[1]} pixels ({size_name}) and saved.")
    print("Displaying resized images. Press any key in the image windows to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("All windows closed. Project completed successfully.")
if __name__ == "__main__":
    main()