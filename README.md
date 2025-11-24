#Delhi Metro Route & Schedule Simulator

## Project Overview
This project is a Python-based application that simulates the **Delhi Metro Rail Corporation (DMRC)** network, specifically focusing on the **Blue Line**, **Blue Line Branch (Vaishali)**, and **Magenta Line**. 

It functions as an intelligent routing agent that helps users find the best path between stations, calculating precise arrival times, interchange points, and total travel duration based on real-world schedule constraints (Peak vs. Off-Peak hours).

## File Structure
* **`metro_simulator.py`**: The main source code containing the search logic, scheduling algorithms, and user interface.
* **`metro_data.txt`**: The knowledge base (database) containing station names, line mappings, and cumulative travel times.
* **`README.md`**: Project documentation.

## Features
1.  **Knowledge Base Integration**: Loads station data dynamically from a text file.
2.  **Intelligent Routing (Search Algorithm)**:
    * **Direct Route**: Finds paths on the same line.
    * **Single Interchange**: Finds connecting paths via *Janakpuri West*, *Botanical Garden*, or *Yamuna Bank*.
    * **Double Interchange**: Solves complex routes (e.g., Magenta to Blue-Branch) via a multi-hop search strategy.
3.  **Dynamic Scheduling**:
    * Calculates train arrival based on current time.
    * **Peak Hours (8-10 AM, 5-7 PM)**: 4-minute frequency.
    * **Off-Peak**: 8-minute frequency.
4.  **Realistic Constraints**: Accounts for a 5-minute walking time buffer during interchanges.

## How to Run
1.  Ensure you have Python installed.
2.  Place `metro_simulator.py` and `metro_data.txt` in the same folder.
3.  Open your terminal or command prompt.
4.  Run the following command:
    ```bash
    python metro_simulator.py
    ```

## Input Format
* **Source Station**: Enter the exact name (case-insensitive).
* **Destination Station**: Enter the exact name.
* **Current Time**: Format `HH:MM` (24-hour format preferred, e.g., `09:30` or `14:15`).

## Example Usage
```text
Source Station: IIT Delhi
Destination Station: Vaishali
Current Time (HH:MM): 10:00

--- Output ---
Double Interchange Route
1. Take Magenta Line at 10:04
2. Switch at Botanical Garden (10:29)
3. Take Blue at 10:34
4. Switch at Yamuna Bank (10:54)
5. Take Blue-Branch at 10:59
6. Arrive Destination at 11:20
Total Time: 76 mins
