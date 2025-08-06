import React from "react";
import './ChildCard.css'

const Dialog = (props) => {
      return (
            <div className="child-card">
                  <b>Dialogue</b>
                  <div>{props.dialog}</div>
            </div>
      )
}

export default Dialog;