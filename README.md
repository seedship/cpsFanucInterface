# cpsFanucInterface

## Setup
* Create New Project - Default options are okay except for the following steps:
    * Step 2: Workcell Name -- Choose a name
    * Step 6: Group 1 Robot Model -- Purchased robot is H753 LR Mate 200iD/7L (R-30iB+ Mate Controller)
    * Step 8: Robot Options -- Add the following
        * KAREL (R632)
        * User Socket Msg (R648)
        * Dyn Path Modifier (R739)

* Set HTTP Authentication to Unlocked
    * Open Teach Pennant
    * Menu -> 6. Setup -> 9. Host Comm (Should be under window 2 number 9 if no additional options were chosen in Setup Step 8)
    * Select number 6. HTTP
    * Set Karel to UNLOCK
    
* Setup DPM
    *  Follow the DPM and Host Comm sections under [Configuration guide](https://github.com/gavanderhoorn/fanuc_dpm_mouse_demo) from the FANUC DPM Mouse Demo
    * Set U Frame
        * Menu -> 6. Setup -> 4. Frames
        * Choose \[Other\] -> 3. User Frames
        * Select SETIND and select 1