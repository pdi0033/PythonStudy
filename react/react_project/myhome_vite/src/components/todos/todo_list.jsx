import {useState, useEffect} from 'react';
import axios from 'axios';

function TodoList() {
    const [todoList, setTodoList] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const loadData =()=>{
        setIsLoading(true);
        fetch('https://jsonplaceholder.typicode.com/todos')
        .then(response => response.json())
        .then(json => {
            console.log(json);
            setTodoList(json);
        })
        .catch(error => {
            console.log("데이터 수신에러");
        })
        .finally( () => {
            // 데이터 수신완료
            setIsLoading(false);
        })
    }

    useEffect( ()=> {
        loadData();
    }, []);

    return ( 
        <div>
            {isLoading? <div>loading...</div>:
            <table>
                {
                    todoList.map( (item, i) =>{
                        return (
                            <tr key={i}>
                                <td>{item.userId}</td>
                                <td>{item.id}</td>
                                <td>{item.title}</td>
                                <td>{item.completed}</td>
                            </tr>
                        )
                    } )
                }
            </table>}
        </div>
    );
}

export default TodoList;