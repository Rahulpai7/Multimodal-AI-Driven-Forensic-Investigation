import React from "react";
import './ChildCard.css'


const AudioSentiment = (props) => {
      return (
            <div className="child-card">
                  <b>Audio Based Emotion</b>
                  <div>{props.audio_sentiment}</div>
            </div>      
      )
}

export default AudioSentiment;