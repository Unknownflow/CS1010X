public class Decision {
    int getRiskLevel(int bp, int gender, int age, int sinus) {
        if (bp > 91) {
            if (gender == 1) {
                if (age > 55) {
                    if (sinus == 1) {
                        return 5;
                    } else {
                        return 4;
                    }
                } else {
                    return 3;
                }
            } else {
                if (age > 63) {
                    if (sinus == 1) {
                        return 5;
                    } else {
                        return 4;
                    }
                } else {
                    return 2;
                }
            }
        } else {
            return 1;
        }
    }
}
