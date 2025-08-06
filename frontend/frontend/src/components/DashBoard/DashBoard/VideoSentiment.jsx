import React from "react";
import src1 from './videos/finvid1.mp4'
import src2 from './videos/finvid2.mp4'
import src3 from './videos/finvid3.mp4'
import src4 from './videos/finvid4.mp4'

const sources = [src2, src1, src3, src4, src4]

const VideoSentiment = (props) => {
      const id = props.id;
      return (
      <div className='video'>
            <video
                  controls
                  src={sources[id-1]}
                  style={{ width: '750%', maxWidth: '700px' }}
            >
                  Couldn't load
            </video>
      </div>
      )
}

export default VideoSentiment;