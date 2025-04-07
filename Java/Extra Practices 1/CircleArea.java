public class CircleArea {
    public double calculateArea(double side) {
        double radius = Math.sqrt(2 * Math.pow(side / 2, 2));
        double area = Math.PI * Math.pow(radius, 2);
        return area;
    }
}
