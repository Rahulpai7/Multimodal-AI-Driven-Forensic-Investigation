# 🔍 Multimodal AI-Driven Forensic Investigation

A comprehensive forensic investigation platform that leverages AI to analyze audio, video, and text evidence for law enforcement and legal professionals.

## 🌟 Features

- **Audio Analysis**: Speech-to-text conversion using OpenAI Whisper
- **Video Processing**: Automatic audio extraction from video files
- **Text Summarization**: AI-powered summarization using fine-tuned BART model
- **Sentiment Analysis**: Dual sentiment analysis for both text and audio
- **Real-time Processing**: FastAPI backend for efficient file processing
- **Modern UI**: React-based frontend with intuitive design
- **Export Capabilities**: Results exported to Excel and text formats

## 🏗️ Architecture

```
├── Backend/                    # FastAPI server
│   ├── foren_summer_bart_large/   # Fine-tuned BART model
│   ├── uploads/                   # File upload directory
│   ├── main.py                   # Main FastAPI application
│   ├── audioSentiment.py         # Audio sentiment analysis
│   ├── textSentiment.py          # Text sentiment analysis
│   ├── summarizer.py             # Text summarization
│   └── ffmpeg.exe                # Video processing tool
├── frontend/frontend/          # React application
│   ├── src/                      # React source code
│   ├── public/                   # Static assets
│   └── dist/                     # Production build
└── README.md                   # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 18+
- Git

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rahulpai7/Multimodal-AI-Driven-Forensic-Investigation.git
   cd "multi modal forsensic investigation"
   ```

2. **Install Python dependencies**
   ```bash
   cd Backend
   pip install fastapi uvicorn loguru moviepy transformers torch pandas openpyxl librosa soundfile
   ```

3. **Start the backend server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend/frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Build for production**
   ```bash
   npm run build
   ```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the Backend directory:
```env
UPLOAD_DIR=uploads
MODEL_PATH=foren_summer_bart_large
```

### API Endpoints
- `POST /uploadfile/` - Upload and process audio/video files
- Base URL: `http://localhost:8000`

## 📱 Usage

1. **Upload File**: Select an audio (.mp3, .wav) or video (.mp4) file
2. **Processing**: The system will:
   - Extract audio from video (if needed)
   - Convert speech to text using Whisper
   - Generate summary using fine-tuned BART
   - Analyze sentiment in both text and audio
3. **Results**: View processed results including:
   - Original transcript
   - AI-generated summary
   - Sentiment analysis scores
   - Audio sentiment metrics

## 🤖 AI Models Used

- **OpenAI Whisper Medium**: Speech recognition
- **Fine-tuned BART Large**: Text summarization
- **Custom Audio Sentiment Model**: Audio emotion analysis
- **Text Sentiment Pipeline**: Text emotion analysis

## 📊 Output Formats

Results are saved in multiple formats:
- **Excel**: `output.xlsx` with structured data
- **Text**: `output.txt` with concatenated results
- **JSON**: API response with all metrics

## 🌐 Deployment

### Netlify (Frontend)
1. Build the project: `npm run build`
2. Deploy the `dist` folder to Netlify
3. Configure redirects for React Router

### Backend Deployment Options
- **Heroku**: For cloud deployment
- **Railway**: Modern deployment platform
- **Local**: For development and testing

## 🔒 Security Features

- File type validation
- Size limits for uploads
- CORS configuration
- Secure file handling

## 🛠️ Development

### Project Structure
```
Backend/
├── main.py              # FastAPI application
├── audioSentiment.py    # Audio analysis module
├── textSentiment.py     # Text analysis module
├── summarizer.py        # Summarization logic
└── uploads/             # File storage

Frontend/
├── src/
│   ├── components/      # React components
│   ├── pages/          # Page components
│   └── App.jsx         # Main application
└── public/             # Static assets
```

### Adding New Features
1. Backend: Add new endpoints in `main.py`
2. Frontend: Create components in `src/components/`
3. Models: Add new AI models in respective modules

## 📈 Performance

- **Processing Speed**: ~30 seconds for 5-minute audio
- **Model Size**: 1.5GB BART model (Git LFS)
- **Supported Formats**: MP3, WAV, MP4
- **Max File Size**: 100MB per upload

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Rahul Pai**
- GitHub: [@Rahulpai7](https://github.com/Rahulpai7)
- Repository: [Multimodal-AI-Driven-Forensic-Investigation](https://github.com/Rahulpai7/Multimodal-AI-Driven-Forensic-Investigation)

## 🆘 Support

For support and questions:
1. Check the [Issues](https://github.com/Rahulpai7/Multimodal-AI-Driven-Forensic-Investigation/issues) page
2. Create a new issue with detailed description
3. Include error logs and system information

## 🔄 Updates

- **v1.0.0**: Initial release with core functionality
- **v1.1.0**: Added Netlify deployment support
- **v1.2.0**: Updated to React 18.3.1 and latest dependencies

---

⭐ **Star this repository if you find it helpful!**