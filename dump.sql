-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 27, 2023 at 03:53 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_herbalsynergy`
--

-- --------------------------------------------------------

--
-- Table structure for table `herb_dtls`
--

CREATE TABLE `herb_dtls` (
  `id` int(11) NOT NULL,
  `part_name` varchar(255) DEFAULT NULL,
  `common_name` varchar(255) DEFAULT NULL,
  `scientific_name` varchar(255) DEFAULT NULL,
  `family` varchar(255) DEFAULT NULL,
  `places_found` varchar(255) DEFAULT NULL,
  `coordinate` varchar(255) DEFAULT NULL,
  `compounds` varchar(255) DEFAULT NULL,
  `medicines` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `shape` varchar(255) DEFAULT NULL,
  `plant_username` varchar(225) NOT NULL,
  `language_id` varchar(225) NOT NULL,
  `image_path` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `herb_dtls`
--

INSERT INTO `herb_dtls` (`id`, `part_name`, `common_name`, `scientific_name`, `family`, `places_found`, `coordinate`, `compounds`, `medicines`, `color`, `size`, `shape`, `plant_username`, `language_id`, `image_path`) VALUES
(2, 'Neem leaf', 'Neem', 'Azadirachta indica', 'mahogany family, Meliaceae', 'India, Sri lanka, Thailand, Malaysia, and Indonesia', 'Uttar Pradesh ,Tamil Nadu, Greater Noida ,Karnataka', 'Nimbin (2-3%), Nimbidin (0.1-0.2%), Azadirachtin (0.5-1.5%), Nimbolide (0.1-0.2%), Quercetin (0.1-0.5%), β-Sitosterol (0.01-0.03%), Salannin (0.1-0.5%), Vitamin C (50-100 mg/100g), Fatty Acids and Amino Acids.', 'Immunomodulatory, Anti-inflammatory, Antiulcer, Antimalarial, Antifungal, Antibacterial, Antiviral, Antioxidant, Anticarcinogenic properties', 'dark green, reddish to purplish in colour(when young).', ' 3-8 cm long.', 'pinnate, slightly curved like sickle, with distinct toothed margin, tapering tips and distinctly asymmetric base', 'neem_leaf', 'english', 'plant_images/neem_leaf.png'),
(3, 'Aloe vera', 'Aloe Vera', 'Aloe barbadensis miller', 'Asphodelaceae', ' Arabian Peninsula, India, Mexico, various parts of Africa', 'Rajasthan, Gujarat\r\n', 'Polysaccharides (0.1-0.2%), Enzymes (0.1-0.2%), Anthraquinones (0.02-0.2%), Vitamins (0.1-0.2%), Minerals (0.1-0.2%), Amino Acids (0.1-0.2%), Sterols (0.05-0.1%), Saponins (0.1-0.2%), Lignin (0.1-0.2%), Glycoproteins (0.1-0.2%) and Salicylic Acid (0.02-0.', 'Soothing and healing properties, Used to treat Burns, Wounds, Sunburn, Eczema, Psoriasis,                 Potential internal health benefits.', 'Fleshy, green leaves', ' 50-100 cm long', 'Long and Tapering leaves filled with clear gel-like substance.', 'aloe_vera', 'english', 'plant_images/aloe_vera.png'),
(4, 'Tulsi leaf', 'Tulsi, Holy basil', 'Ocimum sanctum', 'Lamiaceae', 'Indian subcontinent, Southeast Asia, and Africa.', 'Gujarat', 'Phenolic Compounds (1-2%), Eugenol (up to 1.5%), Ocimarin (0.5-1%), Ursolic Acid (0.2-0.7%), Rosmarinic Acid (0.2-0.7%), Vitamins and Minerals, Essential Oils (up to 0.2%), Tannins (0.1-0.2%)', 'Antioxidants, antimicrobial, anti-inflammatory properties are used to treat respiratory disorders, fever, asthma, stress.', 'Green, aromatic leaves', '2-4 cm long', 'Elliptical or ovate, having serrated edges.', 'tulsi_leaf', 'english', 'plant_images/tulsi_leaf.jpg'),
(5, 'Curry leaves', 'curry leaves', 'Murraya koenigii', 'Rutaceae', ' India and Sri lanka.', 'Himalayas, Maharashtra, Tamil Nadu, Kerala, Assam', 'Alkaloids (0.05-0.15%), Carotenoids (0.01-0.02%), Phenolic Compounds (0.2-0.5%), Flavonoids (0.1-0.3%), Terpenes (up to 1%), Essential Oils (0.2-0.5%), Proteins (1-2%), Fiber (1-2%), Vitamins, Minerals, Amino Acids, Glycosides.', 'Used to treat digestive disorders, Diabetes, Skin conditions, Antioxidant properties, Protect the body against free radicals.', 'Dark green, Very young leaves are reddish to purplish in colour.', '2-4 cm long', 'Pinnate, lance-shaped, with a glossy appearance and a strong, aromatic fragrance', 'curry_leaves', 'english', 'plant_images/curry_leaves.png'),
(6, 'Papaya leaves', 'Papaya leaves', 'Carica papaya', 'Caricaceae', 'Central America and Mexico, cultivated in tropical and subtropical regions around the world', 'Andhra Pradesh, Karnataka, Gujarat, Orissa, West Bengal, Assam, Kerala, Madhya Pradesh', 'Phenolic Compounds (0.1-0.4%), Alkaloids (0.01-0.1%), Proteolytic Enzymes (up to 1%), Vitamins, Minerals, Amino Acids, Fiber (1-2%), Carotenoids, Essential Oils (0.1-0.5%), Tannins (0.1-0.3%)', 'Digestive issues, such as indigestion and constipation, Used for their potential anti-malarial properties.', 'Vibrant green', '20-30 cm', 'Large, palmately lobed', 'papaya_leaves', 'english', 'plant_images/papaya_leaves.png'),
(7, 'Mint', 'Mint', 'Mentha piperit (Peppermint), Mentha spicata (Spearmint), Mentha arvensis (Wild Mint), Mentha viridis (Green Mint)', 'Lamiaceae (Mint family)', 'Europe, Asia, North America, and the Middle East', 'Mumbai, Hyderabad, Kolkata, Uttar Pradesh', 'Menthol (40-80%), Menthone (20-30%), Cineole (1-10%), Limonene (1-5%), α-Pinene and β-Pinene (0.1-1%), Flavonoids (0.5-2%), Tannins (0.5-2%), Carotenoids, Vitamins, Minerals, Essential Oils (0.5-2%), Fiber (1-2%) ', 'Digestive Aid, Respiratory Health, Mint Oil, Oral Health, Antioxidant Properties', 'vibrant shade of green', '2.5 to 5 cm', 'oval to lance-shaped, and the edges are serrated or toothed', 'mint', 'english', 'plant_images/mint.png'),
(8, 'Patharchatta', 'Patharchatta', 'Bryophyllum pinnatum (previously known as Kalanchoe pinnata)', 'Crassulaceae', 'India, Southeast Asia, the Caribbean, and other warm climates', 'Himalayas, Kashmir, Assam', 'Alkaloids (0.2-0.5%), Flavonoids, Triterpenes, Glycosides, Polysaccharides, Vitamins and Minerals, Mucilage, Tannins', 'Wound Healing, Respiratory Conditions, Digestive Disorders, Antioxidant and Immunomodulatory Effects, Anti-Inflammatory Properties', 'Green leaves', '5 to 10 cm', 'typically pinnate', 'patharchatta', 'english', 'plant_images/patharchatta.png');

-- --------------------------------------------------------

--
-- Table structure for table `herb_dtls_guj`
--

CREATE TABLE `herb_dtls_guj` (
  `id` int(11) NOT NULL,
  `part_name` varchar(255) DEFAULT NULL,
  `common_name` varchar(255) DEFAULT NULL,
  `scientific_name` varchar(255) DEFAULT NULL,
  `family` varchar(255) DEFAULT NULL,
  `places_found` varchar(255) DEFAULT NULL,
  `coordinate` varchar(255) DEFAULT NULL,
  `compounds` varchar(255) DEFAULT NULL,
  `medicines` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `shape` varchar(255) DEFAULT NULL,
  `plant_username` varchar(225) NOT NULL,
  `language_id` varchar(225) NOT NULL,
  `image_path` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `herb_dtls_guj`
--

INSERT INTO `herb_dtls_guj` (`id`, `part_name`, `common_name`, `scientific_name`, `family`, `places_found`, `coordinate`, `compounds`, `medicines`, `color`, `size`, `shape`, `plant_username`, `language_id`, `image_path`) VALUES
(2, 'લીમડાનું પાન', 'લીમડો ', 'Azadirachta indica', 'mahogany family, Meliaceae', 'ભારત, શ્રીલંકા, થાઇલેન્ડ, મલેશિયા અને ઇન્ડોનેશિયા', 'Uttar Pradesh ,Tamil Nadu ,Karnataka', 'Nimbin (2-3%), Nimbidin (0.1-0.2%), Azadirachtin (0.5-1.5%), Nimbolide (0.1-0.2%), Quercetin (0.1-0.5%), β-Sitosterol (0.01-0.03%), Salannin (0.1-0.5%), Vitamin C (50-100 mg/100g), Fatty Acids and Amino Acids.', 'રોગપ્રતિક્રિયા મોડ્યુલેટરી, પ્રશમક, અલ્સર વિરોધી, મેલેરિયા વિરોધી, ફંગલ વિરોધી, જીવાણુ વિરોધી, વાયરસ વિરોધી, એન્ટીઑક્સિડન્ટ, કેન્સર વિરોધી', 'ઘાટો લીલો, લાલથી જાંબલી રંગનો(જ્યારે યુવાન હોય ત્યારે).', ' 3-8 સે .મી. લાંબી.', 'પિનેટ, સિકલ જેવા સહેજ વક્ર, અલગ દાંતાદાર માર્જિન, ટેપરિંગ ટીપ્સ અને સ્પષ્ટ રીતે અસમપ્રમાણ આધાર સાથે', 'neem_leaf', 'gujrati', 'plant_images/neem_leaf.png'),
(3, 'કુંવારપાઠું', 'કુંવારપાઠું', 'Aloe barbadensis miller', 'Asphodelaceae', 'અરબી દ્વીપકલ્પ, ભારત, મેક્સિકો, આફ્રિકાના વિવિધ ભાગો', 'Rajasthan, Gujarat', 'Polysaccharides (0.1-0.2%), Enzymes (0.1-0.2%), Anthraquinones (0.02-0.2%), Vitamins (0.1-0.2%), Minerals (0.1-0.2%), Amino Acids (0.1-0.2%), Sterols (0.05-0.1%), Saponins (0.1-0.2%), Lignin (0.1-0.2%), Glycoproteins (0.1-0.2%) and Salicylic Acid (0.02-0.', 'શાંતિ અને ઉપચાર ગુણ, બર્ન, ઘાવ, સૂરયસ્પર્ન, એક્ઝેમા, પ્સોરાયસિસ, સંભાવિત અંતર્ગત આરોગ્ય લાભ.', 'માંસલ, લીલા પાંદડા', '50-100 સે .મી. લાંબી', 'સ્પષ્ટ જેલ જેવા પદાર્થથી ભરેલા લાંબા અને ટેપરિંગ પાંદડા.', 'aloe_vera', 'gujrati', 'plant_images/aloe_vera.png'),
(4, 'તુલસીનું પાન', 'તુલસી, પવિત્ર તુલસી', 'Ocimum sanctum', 'Lamiaceae', 'ભારતીય ઉપખંડ, દક્ષિણપૂર્વ એશિયા અને આફ્રિકા.', 'Gujarat', 'Phenolic Compounds (1-2%), Eugenol (up to 1.5%), Ocimarin (0.5-1%), Ursolic Acid (0.2-0.7%), Rosmarinic Acid (0.2-0.7%), Vitamins and Minerals, Essential Oils (up to 0.2%), Tannins (0.1-0.2%)', 'એન્ટીઑકિસડન્ટો, એન્ટિમાઇક્રોબાયલ અને બળતરા વિરોધી ગુણધર્મો, દગ, ઘાવ, સૂરજ બર્ન, એક્ઝેમા, પ્સોરાયસિસ, અને તણાવ ની સારવાર માટે વપરાય છે', 'લીલા, સુગંધિત પાંદડા', '2-4 સે .મી. લાંબી', 'અંડાકાર અથવા અંડાકાર, દાણાદાર ધાર ધરાવતા.', 'tulsi_leaf', 'gujrati', 'plant_images/tulsi_leaf.jpg'),
(5, 'મીઠો લીમડો', 'મીઠો લીમડો', 'Murraya koenigii', 'Rutaceae', 'ભારત અને શ્રીલંકા.', 'Himalayas, Maharashtra, Tamil Nadu, Kerala, Assam', 'Alkaloids (0.05-0.15%), Carotenoids (0.01-0.02%), Phenolic Compounds (0.2-0.5%), Flavonoids (0.1-0.3%), Terpenes (up to 1%), Essential Oils (0.2-0.5%), Proteins (1-2%), Fiber (1-2%), Vitamins, Minerals, Amino Acids, Glycosides.', 'પાચન વિકૃતિઓ, ડાયાબિટીસ અને ત્વચાની સ્થિતિઓની સારવાર માટે વપરાય છે, એન્ટીઑકિસડન્ટ ગુણધર્મો, શરીરને મુક્ત રેડિકલ સામે રક્ષણ આપે છે.', 'ઘાટો લીલો, ખૂબ જ નાના પાંદડા લાલ રંગના હોય છે.', '2-4 સે .મી. લાંબી', 'ચળકતા દેખાવ અને મજબૂત, સુગંધિત સુગંધ સાથે પિનેટ, લાન્સ-આકારના', 'curry_leaves', 'gujrati', 'plant_images/curry_leaves.png'),
(6, 'પપૈયું', 'પપૈયું', 'Carica papaya', 'Caricaceae', 'મધ્ય અમેરિકા અને મેક્સિકો, વિશ્વભરના ઉષ્ણકટિબંધીય અને ઉષ્ણકટિબંધીય પ્રદેશોમાં ઉગાડવામાં આવે છે', 'Andhra Pradesh, Karnataka, Gujarat, Orissa, West Bengal, Assam, Kerala, Madhya Pradesh', 'Phenolic Compounds (0.1-0.4%), Alkaloids (0.01-0.1%), Proteolytic Enzymes (up to 1%), Vitamins, Minerals, Amino Acids, Fiber (1-2%), Carotenoids, Essential Oils (0.1-0.5%), Tannins (0.1-0.3%)', 'પાચન સમસ્યાઓ, જેમ કે અપચો અને કબજિયાત. તેના સંભવિત મલેરિયા વિરોધી ગુણધર્મો માટે પણ વપરાય છે.', 'સામાન્ય રીતે વાઇબ્રેન્ટ લીલા', '20-30 સે .મી.', 'મોટા, પામલી લોબડ', 'papaya_leaves', 'gujrati', 'plant_images/papaya_leaves.png'),
(7, 'ટંકશાળ', 'ટંકશાળ', 'Mentha piperit (Peppermint), Mentha spicata (Spearmint), Mentha arvensis (Wild Mint), Mentha viridis (Green Mint)', 'Lamiaceae (Mint family)', 'યુરોપ, એશિયા, ઉત્તર અમેરિકા અને મધ્ય પૂર્વ', 'Mumbai, Hyderabad, Kolkata, Uttar Pradesh', 'Menthol (40-80%), Menthone (20-30%), Cineole (1-10%), Limonene (1-5%), α-Pinene and β-Pinene (0.1-1%), Flavonoids (0.5-2%), Tannins (0.5-2%), Carotenoids, Vitamins, Minerals, Essential Oils (0.5-2%), Fiber (1-2%) ', 'પાચન સહાય, શ્વસન આરોગ્ય, ટંકશાળનું તેલ, મૌખિક આરોગ્ય, એન્ટીઑકિસડન્ટ ગુણધર્મો', 'લીલા રંગની વાઇબ્રેન્ટ શેડ', '2.5 થી 5 સે .મી.', 'અંડાકારથી લેન્સ-આકારના, અને કિનારીઓ દાંતાદાર અથવા દાંતવાળી હોય છે', 'mint', 'gujrati', 'plant_images/mint.png'),
(8, 'પથ્થરચટ્ટા', 'પથ્થરચટ્ટા', 'Bryophyllum pinnatum (previously known as Kalanchoe pinnata)', 'Crassulaceae', 'ભારત, દક્ષિણપૂર્વ એશિયા, કેરેબિયન અને અન્ય ગરમ આબોહવા', 'Himalayas, Kashmir, Assam', 'Alkaloids (0.2-0.5%), Flavonoids, Triterpenes, Glycosides, Polysaccharides, Vitamins and Minerals, Mucilage, Tannins', 'ઘા હીલિંગ, શ્વસન શરતો, પાચન વિકૃતિઓ, એન્ટીઑકિસડન્ટ અને ઇમ્યુનોમોડ્યુલેટરી અસરો, બળતરા વિરોધી ગુણધર્મો', 'લીલા પાંદડા', '5 થી 10 સે .મી.', 'સામાન્ય રીતે પિનેટ', 'pattharchatta', 'gujrati', 'plant_images/patharchatta.png');

-- --------------------------------------------------------

--
-- Table structure for table `herb_dtls_hindi`
--

CREATE TABLE `herb_dtls_hindi` (
  `id` int(11) NOT NULL,
  `part_name` varchar(255) DEFAULT NULL,
  `common_name` varchar(255) DEFAULT NULL,
  `scientific_name` varchar(255) DEFAULT NULL,
  `family` varchar(255) DEFAULT NULL,
  `places_found` varchar(255) DEFAULT NULL,
  `coordinate` varchar(255) DEFAULT NULL,
  `compounds` varchar(255) DEFAULT NULL,
  `medicines` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `shape` varchar(255) DEFAULT NULL,
  `plant_username` varchar(225) NOT NULL,
  `language_id` varchar(225) NOT NULL,
  `image_path` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `herb_dtls_hindi`
--

INSERT INTO `herb_dtls_hindi` (`id`, `part_name`, `common_name`, `scientific_name`, `family`, `places_found`, `coordinate`, `compounds`, `medicines`, `color`, `size`, `shape`, `plant_username`, `language_id`, `image_path`) VALUES
(2, 'नीम का पत्ता', 'नीम', 'Azadirachta indica', 'Mahogany family, Meliaceae', 'भारत, श्रीलंका, थाईलैंड, मलेशिया और इंडोनेशिया', 'Uttar Pradesh ,Tamil Nadu ,Karnataka', 'Nimbin (2-3%), Nimbidin (0.1-0.2%), Azadirachtin (0.5-1.5%), Nimbolide (0.1-0.2%), Quercetin (0.1-0.5%), β-Sitosterol (0.01-0.03%), Salannin (0.1-0.5%), Vitamin C (50-100 mg/100g), Fatty Acids and Amino Acids.', 'इम्यूनोमॉड्यूलेटरी, एंटी - इंफ्लेमेटरी, एंटी - अल्सर, एंटीमलेरियल, एंटीफंगल, एंटीबैक्टीरियल, एंटीवायरल, एंटीऑक्सीडेंट और एंटीकार्सिनोजेनिक गुण', 'गहरा हरा, लाल से बैंगनी रंग(जब युवा हो)।', ' 3 -8 सेमी लंबा।', 'पिननेट, सिकल की तरह थोड़ा घुमावदार, अलग - अलग दांतेदार मार्जिन, टेपरिंग टिप्स और स्पष्ट रूप से असममित आधार के साथ', 'neem_leaf', 'hindi', 'plant_images/neem_leaf.png'),
(3, 'घृत कुमारी', 'घृत कुमारी', 'Aloe barbadensis miller', 'Asphodelaceae', 'अरब प्रायद्वीप, भारत, मेक्सिको, अफ्रीका के विभिन्न भाग', 'Rajasthan, Gujarat', 'Polysaccharides (0.1-0.2%), Enzymes (0.1-0.2%), Anthraquinones (0.02-0.2%), Vitamins (0.1-0.2%), Minerals (0.1-0.2%), Amino Acids (0.1-0.2%), Sterols (0.05-0.1%), Saponins (0.1-0.2%), Lignin (0.1-0.2%), Glycoproteins (0.1-0.2%) and Salicylic Acid (0.02-0.', 'सुखदायक और उपचार गुण, जिनका उपयोग जलन, घाव, सनबर्न, एक्जिमा और सोरायसिस के इलाज के लिए किया जाता है।, संभावित आंतरिक स्वास्थ्य लाभ।', 'मांसल, हरी पत्तियाँ', '50 -100 सेमी लंबा', 'स्पष्ट जेल जैसे पदार्थ से भरे लंबे और पतले पत्ते।', 'aloe_vera', 'hindi', 'plant_images/aloe_vera.png'),
(4, 'तुलसी का पत्ता', 'तुलसी, पवित्र तुलसी', 'Ocimum sanctum', 'Lamiaceae', 'भारतीय उपमहाद्वीप, दक्षिण पूर्व एशिया और अफ्रीका।', 'Gujarat', 'Phenolic Compounds (1-2%), Eugenol (up to 1.5%), Ocimarin (0.5-1%), Ursolic Acid (0.2-0.7%), Rosmarinic Acid (0.2-0.7%), Vitamins and Minerals, Essential Oils (up to 0.2%), Tannins (0.1-0.2%)', 'एंटीऑक्सीडेंट, रोगाणुरोधी और विरोधी भड़काऊ गुण।, श्वसन विकारों, बुखार, अस्थमा और तनाव के इलाज के लिए उपयोग किया जाता है।', 'हरे, सुगंधित पत्ते', '2 -4 सेमी लंबा', 'अण्डाकार या अंडाकार, दाँतेदार किनारों वाला।', 'tulsi_leaf', 'hindi', 'plant_images/tulsi_leaf.jpg'),
(5, 'करी पत्ता', 'करी पत्ता', 'Murraya koenigii', 'Rutaceae', 'भारत और श्रीलंका।', 'Himalayas, Maharashtra, Tamil Nadu, Kerala, Assam', 'Alkaloids (0.05-0.15%), Carotenoids (0.01-0.02%), Phenolic Compounds (0.2-0.5%), Flavonoids (0.1-0.3%), Terpenes (up to 1%), Essential Oils (0.2-0.5%), Proteins (1-2%), Fiber (1-2%), Vitamins, Minerals, Amino Acids, Glycosides.', 'पाचन विकारों, मधुमेह और त्वचा की स्थितियों के इलाज के लिए उपयोग किया जाता है, एंटीऑक्सीडेंट गुण, शरीर को मुक्त कणों से बचाते हैं।', 'गहरा हरा, बहुत छोटी पत्तियां लाल रंग की होती हैं जो बैंगनी रंग की होती हैं।', '2 -4 सेमी लंबा', 'एक चमकदार रूप और एक मजबूत, सुगंधित खुशबू के साथ पिननेट, लांस के आकार का', 'curry_leaves', 'hindi', 'plant_images/curry_leaves.png'),
(6, 'पपीते के पत्ते', 'पपीते के पत्ते', 'Carica papaya', 'Caricaceae', 'मध्य अमेरिका और मेक्सिको, दुनिया भर के उष्णकटिबंधीय और उपोष्णकटिबंधीय क्षेत्रों में खेती की जाती है', 'Andhra Pradesh, Karnataka, Gujarat, Orissa, West Bengal, Assam, Kerala, Madhya Pradesh', 'Phenolic Compounds (0.1-0.4%), Alkaloids (0.01-0.1%), Proteolytic Enzymes (up to 1%), Vitamins, Minerals, Amino Acids, Fiber (1-2%), Carotenoids, Essential Oils (0.1-0.5%), Tannins (0.1-0.3%)', 'पाचन संबंधी समस्याएं, जैसे अपच और कब्ज।, इसके संभावित मलेरिया - रोधी गुणों के लिए भी उपयोग किया जाता है।', 'आमतौर पर जीवंत हरा', '20 -30 सेमी', 'बड़ा, खजूर से भरा हुआ', 'papaya_leaves', 'hindi', 'plant_images/papaya_leaves.png'),
(7, 'मिंट', 'मिंट', 'Mentha piperit (Peppermint), Mentha spicata (Spearmint), Mentha arvensis (Wild Mint), Mentha viridis (Green Mint)', 'Lamiaceae (Mint family)', 'यूरोप, एशिया, उत्तरी अमेरिका और मध्य पूर्व', 'Mumbai, Hyderabad, Kolkata, Uttar Pradesh', 'Menthol (40-80%), Menthone (20-30%), Cineole (1-10%), Limonene (1-5%), α-Pinene and β-Pinene (0.1-1%), Flavonoids (0.5-2%), Tannins (0.5-2%), Carotenoids, Vitamins, Minerals, Essential Oils (0.5-2%), Fiber (1-2%) ', 'पाचन सहायता, श्वसन स्वास्थ्य, टकसाल का तेल, मौखिक स्वास्थ्य, एंटीऑक्सीडेंट गुण', 'हरे रंग की जीवंत छाया', '2.5 से 5 सेमी', 'अंडाकार से लांस के आकार में, और किनारों को दाँतेदार या दांतेदार किया जाता है', 'mint', 'hindi', 'plant_images/mint.png'),
(8, 'पथराचाट्टा', 'पथराचाट्टा', 'Bryophyllum pinnatum (previously known as Kalanchoe pinnata)', 'Crassulaceae', 'भारत, दक्षिण पूर्व एशिया, कैरेबियन और अन्य गर्म जलवायु', 'Himalayas, Kashmir, Assam', 'Alkaloids (0.2-0.5%), Flavonoids, Triterpenes, Glycosides, Polysaccharides, Vitamins and Minerals, Mucilage, Tannins', 'घाव भरने, श्वसन संबंधी स्थितियां, पाचन संबंधी विकार, एंटीऑक्सीडेंट और इम्यूनोमॉड्यूलेटरी प्रभाव, विरोधी भड़काऊ गुण', 'हरी पत्तियाँ', '5 से 10', 'आमतौर पर पिननेट', 'pattharchatta', 'hindi', 'plant_images/patharchatta.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `herb_dtls`
--
ALTER TABLE `herb_dtls`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `herb_dtls_guj`
--
ALTER TABLE `herb_dtls_guj`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `herb_dtls_hindi`
--
ALTER TABLE `herb_dtls_hindi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `herb_dtls`
--
ALTER TABLE `herb_dtls`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `herb_dtls_guj`
--
ALTER TABLE `herb_dtls_guj`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `herb_dtls_hindi`
--
ALTER TABLE `herb_dtls_hindi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
