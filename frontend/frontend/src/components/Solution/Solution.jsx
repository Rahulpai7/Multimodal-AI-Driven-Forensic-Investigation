import React from 'react';
import './Solution.css';
import Interrogation from "/src/assets/Images/Interrogation.png";

const Solution = () => {
    return (
      <div className="solution">
        <h2 className="solution-heading">What Do We Do?</h2>
        <div className="solution-content">
          <img src={Interrogation} alt="" />
          <p className="solution-description">
            We specialize in optimizing the interrogation process by accepting
            MP4 recordings and harnessing our advanced summarizing model to
            extract valuable insights. Our technology transcends simple
            transcription, delving deep into the video content capturing the
            interaction between interrogator and witness. Through sophisticated
            analysis, we extract various entities including emotions, both
            conveyed through voice and discernible in the visual cues of the
            video. We distill key discussion points and provide a comprehensive
            summary of the entire conversation. By leveraging our service, you
            can expedite the initial investigation phase, conserving precious
            time and resources. Whether you operate in law enforcement, legal
            proceedings, or any domain necessitating meticulous interrogation
            analysis, our platform offers the efficiency and precision required.
          </p>
        </div>
      </div>
    );
};

export default Solution;