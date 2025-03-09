import React from "react";
import styles from "../styles/Features.module.scss";
import { FaCamera, FaLanguage, FaHistory } from "react-icons/fa";

export default function Features() {
  return (
    <div className={styles.features}>
      <h2>Why Choose Us?</h2>
      <div className={styles.featureList}>
        <div className={styles.featureItem}>
          <FaCamera size={50} />
          <h3>Image Upload</h3>
          <p>Easy image upload & detection.</p>
        </div>
        <div className={styles.featureItem}>
          <FaLanguage size={50} />
          <h3>Accurate Translation</h3>
          <p>Convert scripts into modern text.</p>
        </div>
        <div className={styles.featureItem}>
          <FaHistory size={50} />
          <h3>Historical Preservation</h3>
          <p>Bringing ancient texts to life!</p>
        </div>
      </div>
    </div>
  );
}
