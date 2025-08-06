import React from 'react'
import Summary from './Summary'
import SummarySentiment from './SummarySentiment'
import AudioSentiment from './AudioSentiment'
import VideoSentiment from './VideoSentiment'
import Dialog from './Dialog'
import './DashboardItem.css'

const DashboardItem = (props) => {
  return (
    <div className='dashboard-item'>
      <h3 className='dashboard-item-title'>Case : {props.id}</h3><br></br>
      <div className='grid-item'>
        <Dialog dialog={props.dialog}/>
        <Summary summary={props.summary}/>
        <SummarySentiment summary_sentiment={props.summary_sentiment}/>
        <AudioSentiment audio_sentiment={props.audio_sentiment}/>
      </div>
      <div className='dashboard-item-item'>
        <VideoSentiment className='video-player' video_sentiment={props.video_sentiment} id={props.id}/>
      </div>
    </div>
  )
}

export default DashboardItem