import {useState, useEffect} from 'react';
import axios from 'axios';
import {Link, useNavigate} from 'react-router-dom';

function ScoreList() {
    const [scoreList, setScoreList] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const loadData =()=>{
        setIsLoading(true);
        // setScoreList([...scoreList, {"name":"홍길동", "kor":90, "eng":90, "mat":90}]);
        axios.get("http://127.0.0.1:8000/scoreList")
        .then( (res) => {
            setScoreList(res.data.scoreList);
        })
        .catch( (error) => {
            console.log(error);
        })
        .finally( ()=> {
            setIsLoading(false);
        })
        // setIsLoading(false);
    }

    useEffect( ()=> {
        loadData();
    }, []);

    return ( 
        <div>
            {isLoading? <div>loading...</div>:
            <table>
                {
                    scoreList.map( (item, i) =>{
                        return (
                            <tr>
                                <td>{item.name}</td>
                                <td>{item.kor}</td>
                                <td>{item.eng}</td>
                                <td>{item.mat}</td>
                            </tr>
                        )
                    } )
                }
            </table>}
            <Link to="/score/insert">등록</Link>
        </div>
    );
}

export default ScoreList;