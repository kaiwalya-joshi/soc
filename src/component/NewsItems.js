import React, { Component } from 'react'
import axios from "axios";

export class NewsItems extends Component { 
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(likes, id, title, description, imageurl, newsurl, publishedAt) {
    if(this.state.isToggleOn){
      likes = likes + 1
    } else{
       likes = likes - 1
    };
    console.log(likes);
    let updatedElement = {
      'id': id,
      'title': title,
      'description': description,
      'Newsurl': newsurl,
      'Imageurl': imageurl,
      'publishedAt': publishedAt,
      'likes': likes
    };
    axios.put(`/api/articles/${id}/`, updatedElement).then(() => this.refreshList());
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
    return;
  }

  render() {
    let {id, title, description, imageurl, newsurl, likes, publishedAt} = this.props;
    return (
    <div className="card bg-dark text-white">
        <img src={imageurl} className="card-img-top" alt="..."/>
        <div className="card-body">
            <h5 className="card-title">{title}</h5>
            <br />
            <h5> {likes} likes</h5>
            <br />
            <p className="card-text">{description}</p>

            <div className='d-flex justify-content-between'>
              <a href={newsurl} className="btn btn-primary">Read Full News</a>
              <button className={this.state.isToggleOn ? 'btn btn-success' : 'btn btn-danger'} onClick={() => {this.handleClick(likes, id, title, description, imageurl, newsurl, publishedAt)}}>  {this.state.isToggleOn ? 'Like' : 'Unlike'} </button>
            </div>
        </div>
    </div>
      
    )
  }
}

export default NewsItems
