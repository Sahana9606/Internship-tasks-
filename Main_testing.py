import os
import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Tumor info dictionary (unchanged)
tumor_info = {
    "Astrocytoma": {
        "symptoms": (
            "Persistent headaches, seizures, memory problems or cognitive decline, nausea, "
            "vomiting, weakness or numbness on one side of the body, difficulty with balance or coordination."
        ),
        "solution": (
            "Treatment usually involves surgical removal of the tumor (if accessible), followed by "
            "radiation therapy and/or chemotherapy depending on tumor grade and location. "
            "Regular follow-up and imaging are important."
        ),
        "nearest_hospital": "Manipal Hospitals"
    },
    "Glioblastoma": {
        "symptoms": (
            "Severe and persistent headaches, nausea, vomiting, seizures, personality or cognitive changes, "
            "speech difficulties, weakness or numbness, and problems with coordination or walking."
        ),
        "solution": (
            "Standard treatment includes maximal safe surgical resection, followed by radiation therapy combined "
            "with chemotherapy (usually temozolomide). Prognosis varies but is generally poor due to aggressive nature."
        ),
        "nearest_hospital": "Aster CMI Hospital"
    },
    "Meningioma": {
        "symptoms": (
            "Headaches, vision problems (blurred or double vision), seizures, weakness or numbness in limbs, "
            "hearing loss, and sometimes changes in personality or cognitive function."
        ),
        "solution": (
            "Often treated with surgical removal of the tumor. If surgery is not feasible or tumor is atypical/malignant, "
            "radiation therapy may be used. Some small or asymptomatic meningiomas may be monitored with regular imaging."
        ),
        "nearest_hospital": "Apollo Hospitals"
    },
    "Metastatic": {
        "symptoms": (
            "Symptoms depend on the location and size of the metastatic tumor and may include headaches, seizures, "
            "neurological deficits such as weakness, sensory changes, or speech difficulties, and cognitive impairment."
        ),
        "solution": (
            "Treatment focuses on managing the primary cancer with systemic therapies like chemotherapy or targeted therapy, "
            "along with localized treatments for brain metastases such as surgery, radiation therapy (including stereotactic radiosurgery), or corticosteroids to reduce swelling."
        ),
        "nearest_hospital": "HCG Cancer Centre"
    },
    "Normal": {
        "symptoms": "No tumor detected; no neurological symptoms related to tumor presence.",
        "solution": "No treatment necessary. Maintain regular health check-ups and monitor symptoms if any arise.",
        "nearest_hospital": "Not applicable"
    }
}


class BrainTumorApp(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Brain Tumor Diseases")
        self.master.config(bg="#E6F0FA")
        self.pack(fill=BOTH, expand=True)

        self.selected_image_path = None
        self.predicted_class = None

        self._setup_widgets()
        self._load_logo()

    def _setup_widgets(self):
        # Title Label
        title_label = Label(
            self.master,
            text="Brain Tumor Diseases",
            font=("Arial", 24, "bold"),
            fg="#2E8B57",
            bg="#E6F0FA"
        )
        title_label.pack(pady=15)

        # Frame for images
        self.image_frame = Frame(self.master, bg="#E6F0FA")
        self.image_frame.pack(pady=10)

        # Four image labels side by side
        self.img_labels = []
        for _ in range(4):
            lbl = Label(self.image_frame, bg="white", bd=2, relief="groove", width=250, height=250)
            lbl.pack(side=LEFT, padx=10)
            self.img_labels.append(lbl)

        # Buttons frame
        btn_frame = Frame(self.master, bg="#E6F0FA")
        btn_frame.pack(pady=20)

        # Action buttons with uniform style
        btn_cfg = {
            "width": 18,
            "font": ("Helvetica", 12, "bold"),
            "bg": "#4682B4",
            "fg": "white",
            "activebackground": "#1E90FF",
            "relief": RAISED,
            "bd": 3,
        }

        Button(btn_frame, text="Browse Input", command=self.browse_image, **btn_cfg).grid(row=0, column=0, padx=10, pady=5)
        Button(btn_frame, text="Threshold & Canny", command=self.segment, **btn_cfg).grid(row=0, column=1, padx=10, pady=5)
        Button(btn_frame, text="Classification", command=self.classify, **btn_cfg).grid(row=0, column=2, padx=10, pady=5)

        # Info buttons with different color
        info_btn_cfg = btn_cfg.copy()
        info_btn_cfg.update({"bg": "#32CD32", "activebackground": "#228B22"})

        Button(btn_frame, text="Show Symptoms", command=self.show_symptoms, **info_btn_cfg).grid(row=1, column=0, padx=10, pady=5)
        Button(btn_frame, text="Show Solution", command=self.show_solution, **info_btn_cfg).grid(row=1, column=1, padx=10, pady=5)
        Button(btn_frame, text="Show Nearest Hospital", command=self.show_hospital, **info_btn_cfg).grid(row=1, column=2, padx=10, pady=5)

        # Text box for output messages
        self.text_box = Text(self.master, width=60, height=18, font=("Consolas", 11), bd=2, relief="sunken")
        self.text_box.pack(pady=10)
        self.text_box.insert(END, "Waiting for Results...\n")

    def _load_logo(self):
        try:
            logo_img = Image.open("logo.jfif").resize((250, 250))
            self.logo_imgtk = ImageTk.PhotoImage(logo_img)
            # Set logo in all image labels initially
            for lbl in self.img_labels:
                lbl.config(image=self.logo_imgtk)
                lbl.image = self.logo_imgtk
        except Exception as e:
            print("Logo image not found or error loading:", e)

    def browse_image(self):
        self.text_box.delete(1.0, END)
        self.text_box.insert(END, "Loading Image...\n")

        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.jfif")]
        )
        if not file_path:
            self.text_box.insert(END, "No image selected.\n")
            return

        self.selected_image_path = file_path
        self.text_box.insert(END, f"Selected: {file_path}\n")

        try:
            img = cv2.imread(file_path)
            img_resized = cv2.resize(img, (250, 250))
            img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(img_rgb)
            imgtk = ImageTk.PhotoImage(pil_img)
            self.img_labels[0].config(image=imgtk)
            self.img_labels[0].image = imgtk
        except Exception as e:
            self.text_box.insert(END, f"Error loading image: {e}\n")
            return

        # Median filter preview
        try:
            median_blurred = cv2.medianBlur(img, 5)
            median_resized = cv2.resize(median_blurred, (250, 250))
            median_rgb = cv2.cvtColor(median_resized, cv2.COLOR_BGR2RGB)
            pil_img2 = Image.fromarray(median_rgb)
            imgtk2 = ImageTk.PhotoImage(pil_img2)
            self.img_labels[1].config(image=imgtk2)
            self.img_labels[1].image = imgtk2
            self.text_box.insert(END, "Pre-processing completed successfully (Median filter applied).\n")
        except Exception as e:
            self.text_box.insert(END, f"Error in preprocessing: {e}\n")

    def segment(self):
        if not self.selected_image_path:
            messagebox.showwarning("Warning", "Please load an image first!")
            return

        self.text_box.delete(1.0, END)
        self.text_box.insert(END, "Segmentation Processing...\n")

        try:
            img_org = cv2.imread(self.selected_image_path)
            img_resized = cv2.resize(img_org, (250, 250))
            img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

            # Grayscale conversion
            gray_image = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

            # Binary thresholding
            _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

            # Canny edge detection
            edges = cv2.Canny(img_rgb, 50, 150)

            # Display edges
            edges_pil = Image.fromarray(edges).resize((250, 250))
            edges_imgtk = ImageTk.PhotoImage(edges_pil)
            self.img_labels[2].config(image=edges_imgtk)
            self.img_labels[2].image = edges_imgtk

            # Display binary threshold
            binary_pil = Image.fromarray(binary_image).resize((250, 250))
            binary_imgtk = ImageTk.PhotoImage(binary_pil)
            self.img_labels[3].config(image=binary_imgtk)
            self.img_labels[3].image = binary_imgtk

            self.text_box.insert(END, "Segmentation completed successfully.\n")

        except Exception as e:
            self.text_box.insert(END, f"Error during segmentation: {e}\n")

    def classify(self):
        if not self.selected_image_path:
            messagebox.showwarning("Warning", "Please load an image first!")
            return

        self.text_box.delete(1.0, END)
        self.text_box.insert(END, "Classifying...\n")

        try:
            dataset_path = "./dataset"
            if not os.path.exists(dataset_path):
                self.text_box.insert(END, "Dataset path './dataset' not found.\n")
                return

            class_labels = sorted([name for name in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, name))])
            print("Class labels found:", class_labels)

            model = load_model('trained_model_DNN1.h5')

            img = image.load_img(self.selected_image_path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0) / 255.0

            pred = model.predict(x)
            index = np.argmax(pred)
            predicted_raw = class_labels[index]

            # Normalize predicted string for tumor_info lookup
            normalized_pred = predicted_raw.strip().lower()
            tumor_keys_norm = {k.lower(): k for k in tumor_info.keys()}

            if normalized_pred in tumor_keys_norm:
                self.predicted_class = tumor_keys_norm[normalized_pred]
            else:
                self.predicted_class = predicted_raw
                messagebox.showwarning("Warning", f"Predicted class '{predicted_raw}' not found in tumor info dictionary.")

            self.text_box.insert(END, f"Predicted: {self.predicted_class}\n")
            self.text_box.insert(END, "Now click on Symptoms, Solution or Nearest Hospital buttons to see details.\n")

        except Exception as e:
            self.text_box.insert(END, f"Error in classification: {e}\n")

    def show_symptoms(self):
        if not self.predicted_class:
            messagebox.showinfo("Info", "No classification done yet.")
            return

        symptoms = tumor_info.get(self.predicted_class, {}).get("symptoms", "No information available.")
        self.text_box.delete(1.0, END)
        self.text_box.insert(END, f"Symptoms for {self.predicted_class}:\n\n{symptoms}\n")

    def show_solution(self):
        if not self.predicted_class:
            messagebox.showinfo("Info", "No classification done yet.")
            return

        solution = tumor_info.get(self.predicted_class, {}).get("solution", "No information available.")
        self.text_box.delete(1.0, END)
        self.text_box.insert(END, f"Solution for {self.predicted_class}:\n\n{solution}\n")

    def show_hospital(self):
        if not self.predicted_class:
            messagebox.showinfo("Info", "No classification done yet.")
            return

        hospital = tumor_info.get(self.predicted_class, {}).get("nearest_hospital", "No information available.")
        self.text_box.delete(1.0, END)
        self.text_box.insert(END, f"Nearest hospital for {self.predicted_class}:\n\n{hospital}\n")


if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x800")
    root.resizable(False, False)
    app = BrainTumorApp(root)
    root.mainloop()
