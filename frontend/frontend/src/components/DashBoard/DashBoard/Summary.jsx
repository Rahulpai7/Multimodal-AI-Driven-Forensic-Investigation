import React from "react";
import './ChildCard.css'

const Summary = (props) => {
      return (
            <div className="child-card">
                  <b>Summary</b>
                  <div>{props.summary}</div>
            </div>      
      )
}

export default Summary;