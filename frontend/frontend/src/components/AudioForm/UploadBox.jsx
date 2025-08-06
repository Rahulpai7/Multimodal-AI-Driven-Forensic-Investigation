import { useState } from "react";
import "./AudioForm.css";

const ALLOWED_FILE_TYPES = ['.mp3', '.mp4', '.wav', '.m4a'];
const MAX_FILE_SIZE = 50 * 1024 * 1024; // 50MB

function UploadBox() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [dialogue, setDialogue] = useState("");
  const [textSenti, setTextSenti] = useState("");
  const [audioSenti, setAudioSenti] = useState("");
  const [video, setVideo] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const validateFile = (file) => {
    if (!file) return "Please select a file";
    
    const fileExtension = '.' + file.name.split('.').pop().toLowerCase();
    if (!ALLOWED_FILE_TYPES.includes(fileExtension)) {
      return `File type not supported. Allowed types: ${ALLOWED_FILE_TYPES.join(', ')}`;
    }
    
    if (file.size > MAX_FILE_SIZE) {
      return `File size too large. Maximum size: ${MAX_FILE_SIZE / (1024 * 1024)}MB`;
    }
    
    return null;
  };

  const handleFileInputChange = (event) => {
    setError("");
    const selectedFile = event.target.files[0];
    const error = validateFile(selectedFile);
    
    if (error) {
      setError(error);
      return;
    }
    
    setFile(selectedFile);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    if (!file) {
      setError("Please select a file first");
      return;
    }
    
    setIsLoading(true);
    setError("");
    
    const formData = new FormData();
    formData.append('file_upload', file);

    try {
      const endpoint = "http://localhost:8000/uploadfile";
      const response = await fetch(endpoint, {
        method: "POST",
        body: formData
      });

      const data = await response.json();
      
      if (response.ok) {
        setSummary(data.summary);
        setDialogue(data.dialogue);
        setAudioSenti(data.audioSenti);
        setTextSenti(data.sentiment);
        setVideo(data.video);
      } else {
        setError(data.message || "Error while uploading file");
      }
    } catch (error) {
      setError("Network error. Please try again later.");
      console.error("Upload error:", error);
    } finally {
      setIsLoading(false);
    }

  }

  return (
    <div className="audioform">
      <h1 className="audioform-title">Upload File</h1>
      <form className="upload-tab" onSubmit={handleSubmit}>
        <div className="upload-container">
          <input
            className="upload-tab-upload"
            type="file"
            onChange={handleFileInputChange}
            accept={ALLOWED_FILE_TYPES.join(',')}
            disabled={isLoading}
          />
          {error && <p className="error-message">{error}</p>}
          <button 
            className="upload-tab-submit" 
            type="submit"
            disabled={!file || isLoading}
          >
            {isLoading ? 'Processing...' : 'Upload'}
          </button>
        </div>
      </form>
      
      {(dialogue || summary || textSenti || audioSenti) && (
        <div>
          <h1 className="audioform-title">Results</h1>
          <div className="result-tab">
            {file && file.type.startsWith('audio/') && (
              <audio controls src={URL.createObjectURL(file)} />
            )}
            <div className="result-parent">
              {dialogue && (
                <div className="result-child">
                  <h3>Dialogue</h3>
                  <p>{dialogue}</p>
                </div>
              )}
              {summary && (
                <div className="result-child">
                  <h3>Summary</h3>
                  <p>{summary}</p>
                </div>
              )}
              {textSenti && (
                <div className="result-child">
                  <h3>Text Based Emotion</h3>
                  {Object.entries(textSenti)
                    .sort(([, a], [, b]) => b - a)
                    .map(([key, value]) => (
                      <p key={key}>
                        {key}: {value}%
                      </p>
                    ))}
                </div>
              )}
              <div className="result-child">
                <h3>Audio Based Emotion</h3>
                {Array.isArray(audioSenti) && audioSenti.length > 0 ? (
                  audioSenti.map((item, index) => (
                    <p key={index}>
                      Label: {item.label}, Score: {(item.score * 1000).toFixed(2)}%
                    </p>
                  ))
                ) : (
                  <p>No audio sentiment data available.</p>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default UploadBox;
