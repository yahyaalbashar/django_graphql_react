import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import ListMusic from './list_music/list_music_component'

class App extends Component {
  state={
    music_list:[],
  }
  
  getMusicList(){

    const url="//127.0.0.1:8000/graphql"
    let thisComp=this
    const query={ query:`
                        query{
                        songs{
                          songName
                          album{
                            title
                            artist{
                              name
                            }
                          }
                        }
                      }
                   `
             }
    axios.post(url,query).then(function(response){
      return response
    }).then(function(responseData){
      console.log(responseData.data.data.songs)
      thisComp.setState({
        music_list:responseData.data.data.songs

      })
      
    })
    

  }
  componentDidMount(){
    this.setState({
    music_list:[]  
    })
    
    this.getMusicList()
  }





  render() {
    const {music_list}=this.state
    return (
      <div className="App">
        {music_list.map((song,index)=>{
          return <ListMusic key={`$index`} songname={song.songName} artist={song.album.artist.name} album={song.album.title}/>


        })}
      
      
      </div>
    );
  }
}

export default App;
