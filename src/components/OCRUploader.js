import React, { useState } from "react";

const OCRUploader = () => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file)); // Generate preview URL
  };

  const handleUpload = async () => {
    if (!image) {
      alert("Please select an image first.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setText(data.extracted_text || "No text found.");
    } catch (error) {
      console.error("Error uploading image:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>Upload Image for OCR</h2>

      <input type="file" accept="image/*" onChange={handleFileChange} className="file-input" />

      {preview && <img src={preview} alt="Selected" className="image-preview" />}

      <button onClick={handleUpload} className="extract-btn" disabled={loading}>
        {loading ? "Processing..." : "Extract Text"}
      </button>

      {text && (
        <div className="text-box">
          <h3>Extracted Text:</h3>
          <p>{text}</p>
        </div>
      )}
    </div>
  );
};

export default OCRUploader;
