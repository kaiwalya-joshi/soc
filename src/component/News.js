import React, { Component } from 'react'
import NewsItems from './NewsItems'



export class News extends Component {
  articles = []  
  
  constructor(){
    super();
    this.state = {
      articles : this.articles
    }    
  }

  async componentDidMount(){
    //let url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=cd8b0420d24541a69eff42513ab87798';
    //let data = await fetch(url);
    //let fetchedData = await data.json();
    //this.setState({articles: fetchedData.articles});
    // let data = await axios.get("/api/articles/")
    // this.setState({articles: data.data})
    try{
      let data = await fetch('http://localhost:8000/api/articles/');
      data = await data.json();
      this.setState({articles: data})
      console.log(data)
    } catch (e){
      console.log(e)
    }
  }

  render() {
    let {isLoggedIn} = this.props;
    if (isLoggedIn){
    return (
      <div className='container my-5'>
        <div className='row'>
        {this.state.articles.reverse().map((element) => {return(
          <div className='col-md-4 my-3' key = {element.id}>
              <NewsItems id = {element.id} title = {element.title} description = {element.description} imageurl = {element.Imageurl} newsurl = {element.Newsurl} likes = {element.likes} publishedAt = {element.publishedAt}/>
          </div>
        )})}
        </div>
      </div>
    
    )
        }
  }
}

export default News
