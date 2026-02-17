**Input:** 128-bit message, subkey0, and subkey1

**Steps:**

1. AddKey (before round 1)
2. SubBytes
3. ShiftRows
4. MixColumns
5. AddKey

**Output:** Encrypted result

**To Use:** run `python -m aes_m15219531.build.aes_first_round`
