"use client";
import React from "react";
import Image from "next/image";
// import right
import user1 from "/public/images/profile/user-6.jpg";
import user2 from "/public/images/profile/user-2.jpg";
import user3 from "/public/images/profile/user-3.jpg";
import img1 from "/public/images/blog/blog-img1.jpg";
import img2 from "/public/images/blog/blog-img2.jpg";
import img3 from "/public/images/blog/blog-img3.jpg";
import img4 from "/public/images/blog/task1_1.jpg";
import img5 from "/public/images/blog/task2_1o.png";
import img6 from "/public/images/blog/task3_1o.jpg";
import img7 from "/public/images/blog/task3_1o.jpg";
import img8 from "/public/images/blog/task4_1.jpg";
import { Badge } from "flowbite-react";
import { TbPoint }   from "react-icons/tb";

import { Icon } from "@iconify/react";
import Link from "next/link";

const BlogCardsData = [
  {
    avatar: user1,
    coveravatar: img4,
    title: "Use OCR to read product information like brand name, packaging size, and other details from labels.",
    category: "Extracting Details",
    name: "Georgeanna Ramero",
    view: "9,125",
    comments: "3",
    time: "Mon, Dec 19",
    url:'/sample-page'
  },
  {
    avatar: user2,
    coveravatar: img5,
    read: "2 min Read",
    title:
      "Use OCR to efficiently extract expiry dates and MRP details from printed product labels for automated validation.",
    category: "Expiry Date Validation",
    name: "Georgeanna Ramero",
    view: "4,150",
    comments: "38",
    time: "Sun, Dec 18",
    url:'/sample-page2'
  },
  {
    avatar: user3,
    coveravatar: img6,
    read: "2 min Read",
    title: "Utilize machine learning and IR sensors to recognize product brands and count the number of items.",
    category: "Brand Recognition & Counting",
    name: "Georgeanna Ramero",
    view: "9,480",
    comments: "12",
    time: "Sat, Dec 17",
    url:'/sample-page3'
  },
  {
    avatar: user3,
    coveravatar: img8,
    read: "2 min Read",
    title: "Assess and predict the freshness and remaining shelf life of fruits and vegetables by analyzing various visual patterns, cues, and indicators.",
    category: "Predicting Shelf Life",
    name: "Georgeanna Ramero",
    view: "9,480",
    comments: "12",
    time: "Sat, Dec 17",
    url:'/sample-page4'
  }
];

const BlogCards = () => {
  return (
    <>
      <div className=" flex grid grid-cols-4 gap-30">
        {BlogCardsData.map((item, i) => (
          <div className="lg:col-span-1 " key={i}>
            <Link href={item.url} className="group">
            

<div className="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
    {/* <a href="#"> */}
        <Image className="rounded-t-lg" src={item.coveravatar} alt="" />
    {/* </a> */}
    <div className="p-5">
        {/* <a href="#"> */}
            <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{item.category}</h5>
        {/* </a> */}
        <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">{item.title}</p>
        <p  className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
            Start
             <svg className="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
            </svg>
        </p>
    </div>
</div>

            </Link>
          </div>
        ))}
      </div>
    </>
  );
};

export default BlogCards;
