import React from "react";
import "./Problem.css"; 

const ProblemStatement = () => {
  return (
    <div className="problem-statement">
      <h1>Problem Statement</h1>
      <div className="problem-statement-content">
        <p>
          The initial step in any investigation is crucial. However, there are
          various reasons why it may not go right. It could be due to slow
          procedures, biases towards one party, or even pressure from powerful
          individuals.{" "}
          <p>
            This is why we have introduced AI-driven forensic investigation. Our
            technology aids in interrogation and extracting various aspects of
            the investigation process.
          </p>
        </p>
      </div>
    </div>
  );
};

export default ProblemStatement;
