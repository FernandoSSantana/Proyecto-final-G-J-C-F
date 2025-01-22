import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import "../../styles/tableMenu.css";
import { Link, useNavigate } from "react-router-dom";
import { TabsMenu } from "../component/tabsMenu";

// aqui estara el dropdown para hacer los pedidos

export const TableMenu = () => {

    return (
        <>
            <div className="container contenedorImagen">
                <TabsMenu />
            </div>
        </>
    );
};