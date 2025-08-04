import cv2
import pytesseract
import pandas as pd
import re

# --- Configuration ---
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# --- Function to Extract Details ---
def extract_aadhaar_details(text):
    """
    Parses text extracted from an Aadhaar card image to find specific details.
    """
    details = {
        'Aadhaar Number': None,
        'Date of Birth': None,
        'Gender': None
    }

    # Regex for Aadhaar Number
    aadhaar_pattern = r'\b\d{4}\s?\d{4}\s?\d{4}\b'
    match = re.search(aadhaar_pattern, text)
    if match:
        details['Aadhaar Number'] = match.group(0).replace(" ", "")

    # Regex for Date of Birth
    dob_pattern = r'DOB:\s*(\d{2}/\d{2}/\d{4})'
    match = re.search(dob_pattern, text, re.IGNORECASE)
    if match:
        details['Date of Birth'] = match.group(1)

    # Regex for Gender
    gender_pattern = r'(Male|Female|Transgender)'
    match = re.search(gender_pattern, text, re.IGNORECASE)
    if match:
        details['Gender'] = match.group(0).capitalize()

    return details


# --- Main script logic ---

# Initialize image variable
image = None

# Ask the user for their choice
print("Choose an option:")
print("1: Scan document using webcam")
print("2: Use an existing image file")
choice = input("Enter your choice (1 or 2): ")

# --- Option 1: Webcam Input ---
if choice == '1':
    cap = cv2.VideoCapture(0)
    print("\nWebcam opened. Aim at the document.")
    print("Press 's' to scan and process.")
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image from webcam.")
            break
        
        cv2.imshow("Webcam - Press 's' to Scan, 'q' to Quit", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            image = frame  # Assign the captured frame to the image variable
            print("Image captured!")
            break
        elif key == ord('q'):
            print("Quitting webcam.")
            break
            
    cap.release()
    cv2.destroyAllWindows()

# --- Option 2: File Path Input ---
elif choice == '2':
    # Use input() to get the path from the user
    image_path = input("Please enter the full path to your image file: ")
    # Load the image using OpenCV
    image = cv2.imread(image_path)

# --- Invalid Choice ---
else:
    print("Invalid choice. Please run the script again and enter '1' or '2'.")


# --- Process the image if one was successfully loaded or captured ---
if image is not None:
    # Convert the image to grayscale and perform OCR
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    full_text = pytesseract.image_to_string(gray)

    print("\n--- Raw Extracted Text ---")
    print(full_text)
    print("--------------------------\n")

    # Parse the text to get structured details
    extracted_details = extract_aadhaar_details(full_text)

    print("--- Extracted Details ---")
    print(extracted_details)
    print("-------------------------\n")

    # Save the extracted details to a CSV file
    if any(extracted_details.values()): # Check if any detail was found
        df = pd.DataFrame([extracted_details])
        df.to_csv('aadhaar_details.csv', index=False)
        print("Aadhaar details have been saved to aadhaar_details.csv")
    else:
        print("No details could be extracted. The CSV file was not created.")
else:
    print("\nNo image was processed.")
