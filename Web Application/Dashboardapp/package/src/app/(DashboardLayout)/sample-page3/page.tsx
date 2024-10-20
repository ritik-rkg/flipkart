"use client";
import React, { useEffect, useState } from 'react';
import WebcamCapture from '../../(DashboardLayout)/cameraopen/page'; // Adjust path accordingly
import { Badge } from "flowbite-react";
import img1 from "/public/assets/banana3.jpg";
import Image from "next/image";
const imageDetails = {
  productName: "Banana Robusta",
  brandName: "Banana",
  description: "Green skin that turns yellow as it ripens and has creamy white flesh inside.",
  mrp: "34",
  category: "Fruit",
  productId: "I7U98kjn",
  unit: 4,
  seller:"Moonstone Ventures LLP, New Delhi Gadaipur-110030, India"

  // src:
};

const SamplePage = () => {
  const [showWebcam, setShowWebcam] = useState(true);

  useEffect(() => {
    // Set a timer to switch from the webcam to the product details after 10 seconds
    const timer = setTimeout(() => {
      setShowWebcam(false);
    }, 6000); // 10 seconds

    return () => clearTimeout(timer); // Clear the timer on component unmount
  }, []);

  return (
    <>
      {showWebcam ? (
        <WebcamCapture /> // Display WebcamCapture for 10 seconds
      ) : (
        <div className="max-w-6xl mx-auto bg-gray-100 rounded-xl shadow-lg overflow-hidden m-6 flex flex-col md:flex-row">
          <div className="md:w-1/2">
            <Image
              className="w-full h-full object-cover"
              src={img1}
              alt={imageDetails.productName}
            />
          </div>
          <div className="md:w-1/2 p-8 md:p-12">
            <div className="bg-white rounded-lg shadow-sm p-8">
              <h2 className="text-3xl font-bold text-gray-800 mb-6">{imageDetails.productName}</h2>
              <p className="text-lg text-gray-600 mb-6 leading-relaxed">{imageDetails.description}</p>
              <div className="space-y-1.5">
                <p className="text-md text-gray-500">
                  <span className="font-semibold">Name:</span> {imageDetails.brandName}
                </p>
                 <p className="text-md text-gray-500">
                  <span className="font-semibold">Product ID:</span> {imageDetails.productId}
                </p>                
                <p className="text-md text-gray-500">
                  <span className="font-semibold">Category:</span> {imageDetails.category}
                </p>
                <p className="text-md text-gray-500">
                  <span className="font-semibold">Unit:</span> {imageDetails.unit} pieces
                </p>               
                <p className="text-md text-gray-500">
                  <span className="font-semibold">MRP:</span> {imageDetails.mrp}
                </p>               
                 <p className="text-md text-gray-500">
                  <span className="font-semibold">Seller:</span> {imageDetails.seller}
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default SamplePage;
