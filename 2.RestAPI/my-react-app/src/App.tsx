import './App.css'
import {useGetCategoriesQuery} from "./services/apiCategory.ts";

const App = () => {

    const {data: list, isLoading, error} = useGetCategoriesQuery();

    console.log("List items in server", list);

    if (isLoading) {
        return <div>Loading...</div>;
    }
    if (error)
        return <div>Something went wrong.</div>;

    return (
        <>
            <h1>Привіт козаки</h1>

            <table>
                <thead>
                <tr>
                    <th>#</th>
                    <th>Назва</th>
                    <th>Слаг</th>
                    <th>Опис</th>
                </tr>
                </thead>
                <tbody>
                {list?.map((item) => (
                    <tr key={item.id}>
                        <td>{item.id}</td>
                        <td>{item.name}</td>
                        <td>{item.slug}</td>
                        <td>{item.description}</td>

                    </tr>
                ))}
                </tbody>
            </table>


        </>
    )
}

export default App
