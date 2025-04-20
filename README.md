# SEV-scheduler
This Python script finds the (give or take optimal) schedule to ride all specified buses (of rail replacement services) and return to the starting point in the shortest time possible/reasonable, using a priority queue-based approach.

## Usage
1. **Dependencies**: Python 3.x (no external libraries required).
2. **Run the script**:
   ```bash
   python bus_scheduler.py
   ```
3. **Customize**: Modify desired start_time and start_location in the __main__ block and adjust the buses dictionary (at the top of the script) to add/remove routes or change timetables

## Example output
```bash
Best schedule:
Bus 2: Dinslaken (13:01) → Voerde (13:12)
Bus 2: Voerde (13:12) → Friedrichsfeld (Ersatz) (13:22)
Bus 1: Friedrichsfeld (Ersatz) (13:40) → Voerde (13:50)
Bus 5: Voerde (14:50) → Dinslaken (15:04)
Bus 83: Dinslaken (15:30) → Duisburg Hbf (16:00)
Bus 82: Duisburg Hbf (16:05) → Dinslaken (16:35)
Bus 4: Dinslaken (17:04) → OB-Holten (17:19)
Bus 3: OB-Holten (17:45) → Dinslaken (18:01)
Bus 81: Dinslaken (18:10) → Duisburg Hbf (18:40)
Bus 85: Duisburg Hbf (18:45) → Dinslaken (19:15)
Bus 84: Dinslaken (19:30) → Duisburg Hbf (20:00)
Bus 84: Duisburg Hbf (20:05) → Dinslaken (20:35)
Total time: 07:34 h
```

## Current limits / Roadmap
- Overnight rail replacement services might not work because I haven't tested the correctness of overnight time calculation
- You have to copy each time and bus stop manually out of the Excel file into the script. Could be improved by importing .tsv files (easier to code) or directly from the Excel file (harder to code)
- adjustments to the schedule due to delays not possible
- testing of less than all buses not possible
