import React from "react";
import DashboardItem from "./DashboardItem";
import { data } from "./data";
import './Dashboard.css'

const Dashboard = () => {
  return (
    <div className="dashboard">
      <div className="dashboard-page-title">
        <h1>Dashboard</h1>
      </div>
      {data.map((item) => (
        <DashboardItem key={item.id} id={item.id} summary={item.summary} dialog={item.dialogue} audio_sentiment={item.audio_sentiment} video_sentiment={item.video_sentiment} summary_sentiment={item.summary_sentiment} video_source={item.video_source}/>
      ))}
    </div>
  );
};

export default Dashboard;
