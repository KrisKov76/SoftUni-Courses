SELECT
    REPLACE(mountain_range, 'a', '@') AS replace_a,
    REPLACE(mountain_range, 'A', '$') AS replace_А
 FROM
    mountains;


-- replace е case sensitive и затова ще промени само тези букви, които сме му казали


