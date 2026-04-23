import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.io.ByteArrayOutputStream;
import java.security.*;
import java.util.Base64;

public class ExerciseMain {

    protected static String toHexString(byte[] data, int offset) {
        //sorgt dafÃ¼r das Offset immer gÃ¼ltig ist. Wenn Offset negativ ist
        if (offset <0) {
            //wird Offset auf 0 gesetzt
            offset=0;
        }

        //erzeugt StringBuilder-Objekt, um Hexadezimal-String schrittweise aufzubauen
        //effizienter als Verkettung von Strings mit Plus-Operator
        StringBuilder sb = new StringBuilder();

        //geht durch jedes Byte im Byte-Array
        for (int i=0; i<data.length; i++) {
            //jedes Byte wird in zweistelligen Hexadezimalwert umgewandelt
            sb.append(String.format("%02X", data[i]));
            //wenn Offset grÃ¶ÃŸer 0 ist und aktuelle Position (i+1) kleiner als die LÃ¤nge von data und Offset an aktueller Position (i+1) teilbar ist
            if ((offset >0) && (i+1<data.length) && ((i+1) % offset == 0)) {
                //fÃ¼gt Leerzeichen hinzu
                sb.append(" ");
            }
        }
        //gibt Hexadezimal-String zurÃ¼ck
        return sb.toString();
    }

    // Print a nice headline/separator.
    protected static void printHeadline(String headline, String symbol) {
        int width=130;
        String s = symbol;

        if (s.length() != 1) {
            s = " ";
        }
        System.out.println();
        System.out.println(s.repeat(width));
        System.out.println(s + " " + headline);
        System.out.println(s.repeat(width));
        System.out.println();
    }

    protected static void printHeadline(String headline) {
        printHeadline(headline, "=");
    }
    /*protected static byte[] sha256(byte[] data) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        return digest.digest(data);
    }*/
    protected static void aufgabe1() {
        printHeadline("Aufgabe 1: Kryptografische Hash-Funktionen.");

        try {
            /*******************************************************************
             * Teilaufgabe a
             *******************************************************************/
            String nachricht = "Verschlüssel diesen Text.";
            byte[] hash = nachricht.getBytes("UTF-8");

            // Prüfsumme berechnen
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] encryptedHash = digest.digest(hash);
            System.out.println(nachricht);
            System.out.println(toHexString(encryptedHash, 4));

            /*******************************************************************
             * Teilaufgabe b) Prüfsumme verifizieren
             *******************************************************************/
            byte[] empfangenerHash = hash;

            boolean istGueltig = MessageDigest.isEqual(hash, empfangenerHash);

            System.out.println();
            System.out.println(istGueltig);
            /*******************************************************************
             * Teilaufgabe b
             *******************************************************************/

        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    protected static void aufgabe2() {
        printHeadline("Aufgabe 2: Symmetrische VerschlÃ¼sselung.");

        try {
            /*******************************************************************
             * Teilaufgabe a
             *******************************************************************/

            /*******************************************************************
             * Teilaufgabe b
             *******************************************************************/


        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    protected static void aufgabe3() {
        printHeadline("Aufgabe 3: Asymmetrische VerschlÃ¼sselung.");

        try {
            /*******************************************************************
             * Teilaufgabe a
             *******************************************************************/


            /*******************************************************************
             * Teilaufgabe b
             *******************************************************************/

        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    protected static void aufgabe4() {
        printHeadline("Aufgabe 4: Digitale Signaturen.");

        try {
            /*******************************************************************
             * Teilaufgabe a
             *******************************************************************/

            /*******************************************************************
             * Teilaufgabe b
             *******************************************************************/

        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) throws Exception {

        aufgabe1();
        aufgabe2();
        aufgabe3();
        aufgabe4();

    }
}