import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './style.css';

const StoryList = () => {
    const [stories, setStories] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/top-stories')
            .then(response => setStories(response.data))
            .catch(error => console.error("Error fetching data:", error));
    }, []);

    console.log(stories)

    return (
        <div className='container'>
            <h1 className='heading'>Top 10 New Stories</h1>
            <ul className='main-container'>
                {stories.map((story, index) => (
                    <li className='stories' key={index}>
                        <a href={story.url}>{story.title}</a><br />
                        <span>Author: {story.author}</span><br />
                        <span>Score: {story.score}</span><br />
                        <span>Time: {story.time}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default StoryList;
