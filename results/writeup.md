1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

phase1.txt represents the most active period based on two key metrics: average heart rate and range. Phase1 had the highest average heart rate at 87.30 bpm, compared to phase0 (64.59 bpm), phase2 (85.18 bpm), and phase3 (60.65 bpm). Additionally, phase1 had the highest median of 88.5 bpm, further confirming consistently elevated heart activity throughout that recording window.

According to the American Heart Association, the target heart rate zone for a 30-year-old during moderate to vigorous physical activity is 95–162 bpm. heart Phase1's average of 87.30 bpm falls just below this range, suggesting the participant was approaching moderate-intensity activity — likely light exercise or an elevated state of physical exertion. In contrast, phase0 and phase3 averaged 64.59 bpm and 60.65 bpm respectively, which fall within the normal resting heart rate range of 60–100 bpm, indicating periods of rest or low activity. Phase2's average of 85.18 bpm is comparable to phase1, but phase1's higher median and range of 54 bpm versus phase2's 63 bpm suggest phase1 captured a more dynamic and sustained active period overall.

2) Which file had the **poorest** data quality? How do you know?

Dphase0.txt had the poorest data quality. When the clean_heartrate_data function processed each file, it tracked the number of removed (malformed or invalid) records per file. phase0 had the highest number of removed values compared to the other files, indicating it contained the most corrupted or unreadable entries that failed the digit validation check. This means a greater portion of phase0's raw data could not be used in any statistical calculations, making it the least reliable dataset in the pipeline. Poor data quality at this scale is a concern for the machine learning team downstream, as missing or removed records can introduce bias or gaps in pattern recognition for sleep and exercise analysis.

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.

The range of this dataset is 112 bpm.

b) Explain how the extreme value affects the range.

The extreme value of 180 bpm significantly inflates the range. Without the sensor glitch value, the range of the remaining values (68 through 75) would only be 7 bpm, which accurately reflects how tightly clustered the readings are. Because the range is calculated using only the minimum and maximum values, it is highly sensitive to outliers — a single erroneous reading is enough to make the dataset appear far more variable than it actually is.

c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

The interquartile range (IQR) would be a better measure of typical variability for this dataset. The IQR measures the spread of the middle 50% of values, meaning it ignores the bottom 25% and top 25% of the data entirely. This makes it resistant to outliers like the 180 bpm sensor glitch. In this case, the IQR would reflect the variability among the tightly clustered values between 68 and 75 bpm, giving the machine learning team a much more accurate picture of the participant's true heart rate variability during that recording period.