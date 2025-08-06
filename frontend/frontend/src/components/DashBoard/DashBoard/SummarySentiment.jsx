import React from "react";
import './ChildCard.css'

const SummarySentiment = (props) => {
      return (
            <div className="child-card">
                  <b>Summary Based Emotion</b>
                  <div>{props.summary_sentiment}</div>
            </div>      
      )
}

export default SummarySentiment;