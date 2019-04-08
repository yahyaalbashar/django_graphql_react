import React, { Component } from 'react';


class ListMusic extends Component {



  render() {

    const {songname}=this.props
    const {artist}=this.props
    const {album}=this.props
    return (
      <div >
      <h1>song: {songname}</h1>
      <h2>artist: {artist}</h2>
      <h3>album : {album}</h3>
      </div>
    );
  }
}

export default ListMusic;
