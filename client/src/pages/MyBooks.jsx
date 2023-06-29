import React from "react";
import Navbar from "../components/UI/Navbar/Navbar";
import AccountInfo from "../components/UI/AccountInfo/AccountInfo";
import style from "../styles/MyBooks.module.css"
import BooksGrid from "../components/UI/BooksGrid/BooksGrid";

const MyBooks = () => {
    return (
        <div className={"page"}>
            <Navbar/>
            <div className={style.container}>
                <div className={style.leftpanel}>
                    <div className={style.account}>
                        <AccountInfo/>
                    </div>
                    <div className={style.otherOptions}>
                        <button className={style.myRevBtn}>My reviews</button>
                        <button className={style.wantToReadBtn}>Want to read</button>
                    </div>
                </div>
                <div className={style.booksgrid}>
                    <BooksGrid/>
                </div>
            </div>
        </div>
    )
}

export default MyBooks;