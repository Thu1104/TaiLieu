import java.util.Scanner;
import java.util.InputMismatchException;
class LuyThua {
    public static void main(String[] args) {
        while (true) {
            try {
                //Nhap x va n
                Scanner kb = new Scanner(System.in);
                System.out.print("Nhap x: ");
                float x = kb.nextFloat();
                System.out.print("Nhap n: ");
                int n = kb.nextInt();
                //Tinh luy thua x^n
                float ketqua = (float)Math.pow(x,n);
                //Hien thi ra man hinh
                System.out.println(x + " ^ " + n + " = " + ketqua);
                break;
            } catch (InputMismatchException e) {
                System.out.println("Nhap sai kieu du lieu - Nhap lai!!!");
            }
        }
    }
}