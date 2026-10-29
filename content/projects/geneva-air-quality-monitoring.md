---
title: Geneva Air Quality Monitoring Model
category: Senior Design Project
year: "2026"
order: 1
summary: "Production-ready air-quality monitoring station for deployment near landfills in Geneva, NY — redesigned enclosures, sensors, PCB, and a cloud data pipeline."
tags: [Fusion 360, 3D Printing, Pugh Matrix, Environmental Testing]
thumbnail: /static/images/thumbs/air-quality-station.jpg
---

## Project Overview

The goal of this project was to improve and advance BluePrint Geneva’s air-quality monitoring station into a production-ready system for deployment near landfills in Geneva, NY. Building on the previous year’s design, in a team of 4, we evaluated and redesigned the mechanical, electrical, and software systems to improve sensor accuracy, environmental durability, manufacturability, and data accessibility. Mechanical improvements included redesigned interior and exterior enclosures and enhanced insect and weather protection, while the electrical system incorporated more accurate infrared and electrochemical sensors, a custom PCB, and a mains-powered system. On the software side, we developed a cloud-based data pipeline connecting the sensing package, backend, database, and web dashboard, enabling users to view and export sensor data remotely. The resulting system provides a foundation for long-term monitoring of landfill-related air pollutants, with future work focused on manufacturing optimization, sensor calibration, user interface improvements, and remote deployment.

![The deployed air quality system](/static/images/deployed.png)

## Mechanical Project Scope

The project objective was to develop a **maintainable, repeatable air-quality ground sensor** capable of monitoring five compounds. Our team focused on the **sensors, power supply, data connectivity, PCB and sensor housing, and exterior enclosure**.

For the mechanical system, we designed the interior and exterior enclosures around key requirements from our community partners: **maintainability, weather resistance, adequate airflow, and low-cost manufacturing**. The modular, 3D-printed design allows components to be easily accessed, cleaned, and replaced, while the design can transition to injection molding for high-volume production. We also incorporated insect-resistant mesh into the exterior enclosure, selecting the mesh through **community partner input and a Pugh matrix evaluation**.

![CAD rendering and split view of exterior enclosure](/static/images/CAD.png)

## Mechanical Technological Development

Redesigned the interior and exterior enclosures to improve **stability, airflow, weather resistance, and maintainability** while maintaining a cost-effective 3D-printed design. The exterior enclosure was widened and shortened, with redesigned gills and a sloped top to improve airflow and protect internal electronics from weather. The interior enclosure was redesigned with an overlapping lip and integrated base for improved stability and assembly.

Selected an insect-resistant mesh in collaboration with community partners and conducted airflow testing to verify that it would not restrict sensor performance. We then performed two rounds of simulated rain testing using a full enclosure assembly, with results showing **no water penetration into the interior enclosure** during the controlled rain test. Based on these results, the design was advanced to full-system testing and deployment.

![Test results](/static/images/testing.png)

## Mechanical Plan For Next Steps

The mechanical design saw significant changes to both the exterior and interior enclosure, but there can always be improvements. The community partners have emphasized their desire to create a repeatable product. Our recommendation is to design the components in a way that is compatible with injection molding drafting and mold requirements. If repeatable means they want to move to a high volume production design, the fasteners (bolts and heat set inserts) are not the most efficient choice, so we recommend a plastic-snap fastener design. Additionally, we recommend giving the interior more structural integrity than just Velcro. Due to the nature of this class, a large barrier we had was lack of time to make multiple revisions to the design once the proof of concept was solidified.

![The constructed interior enclosure with the PCB](/static/images/InteriorEnclosure.png)
