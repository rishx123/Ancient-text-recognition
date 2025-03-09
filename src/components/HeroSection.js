import React from "react";
import styles from "../styles/HeroSection.module.scss";

export default function HeroSection() {
  return (
    <div className={styles.hero}>
      <h1>Ancient Script Recognition</h1>
      <p>Upload an image and translate ancient scripts instantly!</p>
    </div>
  );
}
