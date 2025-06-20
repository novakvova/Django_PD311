import './App.css'
import HomePage from "./pages/Home";
import {Route, Routes} from "react-router-dom";
import Layout from "./components/Layout";
import * as React from "react";
import AdminLayout from "./layout/admin/AdminLayout.tsx";
import AdminDashboardPage from "./pages/admin/Dashboard";

const App : React.FC = () => {

    return (
        <>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<HomePage />} />
                </Route>

                <Route path={"admin"} element={<AdminLayout />}>

                    <Route path="home" element={<AdminDashboardPage />}/>

                </Route>

            </Routes>
        </>
    )
}

export default App
