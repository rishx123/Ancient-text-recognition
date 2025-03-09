import React, { useState } from "react";

const UploadBox = () => {
  const [image, setImage] = useState(null);
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    setImage(event.target.files[0]);
    setText(""); // Reset text when a new file is selected
    setError(""); // Reset errors
  };

  const handleUpload = async () => {
    if (!image) {
      alert("Please select an image first.");
      return;
    }

    setLoading(true); // Start loading indicator
    setError(""); // Reset previous errors

    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Server Error: ${response.status}`);
      }

      const data = await response.json();
      console.log("OCR API Response:", data);

      if (data.extracted_text) {
        setText(data.extracted_text);
      } else {
        setText("No text extracted. Try another image.");
      }
    } catch (error) {
      console.error("Error uploading image:", error);
      setError("Failed to extract text. Please try again.");
    } finally {
      setLoading(false); // Stop loading indicator
    }
  };

  return (
    <div className="flex flex-col items-center bg-white shadow-lg p-6 rounded-lg">
      <h2 className="text-xl font-semibold mb-4">Upload an Image for OCR</h2>
      <input type="file" accept="image/*" onChange={handleFileChange} className="mb-2" />
      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded-lg"
        disabled={loading}
      >
        {loading ? "Processing..." : "Extract Text"}
      </button>
      {error && (
        <div className="mt-4 p-2 border rounded bg-red-100 w-full text-center text-red-600">
          <p>{error}</p>
        </div>
      )}
      {text && (
        <div className="mt-4 p-2 border rounded bg-gray-100 w-full text-center">
          <h3 className="font-semibold">Extracted Text:</h3>
          <p>{text}</p>
        </div>
      )}
    </div>
  );
};

export default UploadBox;
