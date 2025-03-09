import React from "react";
import HeroSection from "./components/HeroSection";
import UploadBox from "./components/UploadBox";
import Features from "./components/Features";
import CTA from "./components/CTA";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div>
      <HeroSection />
      <UploadBox /> {/* Now includes OCR functionality */}
      <Features />
      <CTA />
      <Footer />
    </div>
  );
}
