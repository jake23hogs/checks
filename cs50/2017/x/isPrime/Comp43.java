
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author shackletonjoshua18
 */
public class Comp43 {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("What is the scale? (F = Fahrenheit, C = Celsius, K = Kelvin, Re = Reaumur, Ra = Rankine ");
        String scale = reader.next();
        System.out.println("What is the temperature? ");
        int temperature = reader.nextInt();
        
        switch(scale) {
            case "F":
                double cfTemp = convertToCelsius(scale, temperature);
                double kfTemp = convertToKelvin(scale, temperature);
                double refTemp = convertToReaumur(scale, temperature);
                double rafTemp = convertToRankine(scale, temperature);
                
                System.out.print(temperature + "  Fahreheit is equivalent to: \n" +
                                                    cfTemp + " in Celsius; " +
                                                    kfTemp + " in Kelvin; " +
                                                    refTemp + " in Reaumur; " +
                                                    rafTemp + " in Rankine.");
                break;
            case "C":
                double kcTemp = convertToKelvin(scale, temperature);
                double recTemp = convertToReaumur(scale, temperature);
                double racTemp = convertToRankine(scale, temperature);
                double fcTemp = convertToFahrenheit(scale, temperature);
                
                System.out.print(temperature + "  Celsius is equivalent to: \n" +
                                                    kcTemp + " in Kelvin; " +
                                                    recTemp + " in Reaumur; " +
                                                    racTemp + " in Rankine; " +
                                                    fcTemp + " in Fahrenheit.");
                break;
            case "K":
                double ckTemp = convertToCelsius(scale, temperature);
                double rekTemp = convertToReaumur(scale, temperature);
                double rakTemp = convertToRankine(scale, temperature);
                double fkTemp = convertToFahrenheit(scale, temperature);
                
                System.out.print(temperature + "  Kelvin is equivalent to: \n" +
                                                    ckTemp + " in Celsius; " +
                                                    rekTemp + " in Reaumur; " +
                                                    rakTemp + " in Rankine; " +
                                                    fkTemp + " in Fahrenheit.");
                break;
            case "Re":
                double creTemp = convertToCelsius(scale, temperature);
                double kreTemp = convertToKelvin(scale, temperature);
                double rareTemp = convertToRankine(scale, temperature);
                double freTemp = convertToFahrenheit(scale, temperature);
                
                System.out.print(temperature + "  Reaumur is equivalent to: \n" +
                                                    creTemp + " in Celsius; " +
                                                    kreTemp + " in Kelvin; " +
                                                    rareTemp + " in Rankine; " +
                                                    freTemp + " in Fahrenheit.");
                break;
            case "Ra":
                double craTemp = convertToCelsius(scale, temperature);
                double kraTemp = convertToKelvin(scale, temperature);
                double reraTemp = convertToReaumur(scale, temperature);
                double fraTemp = convertToFahrenheit(scale, temperature);
                
                System.out.print(temperature + "  Rankine is equivalent to: \n" +
                                                    craTemp + " in Celsius; " +
                                                    kraTemp + " in Kelvin; " +
                                                    reraTemp + " in Reaumur; " +
                                                    fraTemp + " in Fahrenheit.");
                break;
            default:    
                //just run again!
        }
        
        
        //check for what type is input, convert to other 4
    }
    public static double convertToFahrenheit(String scale, int temperature) {
        double fTemp = 0;
        
        if(scale.equalsIgnoreCase("c")) {
            fTemp = 1.8 * temperature + 32;
        } else if (scale.equalsIgnoreCase("K")) {
            fTemp = 1.8* (temperature - 273) + 32;
        } else if (scale.equalsIgnoreCase("re")) {
            fTemp = 2.25 * temperature + 32;
        } else if (scale.equalsIgnoreCase("Ra")) {
            fTemp = temperature - 459.67;
        }
    
        return fTemp;
    }
    public static double convertToCelsius(String scale, int temperature) {
        double cTemp = 0;
        
        if(scale.equalsIgnoreCase("f")) {
            cTemp = (temperature - 32) * 5/9;
        } else if (scale.equalsIgnoreCase("K")) {
            cTemp = temperature - 273.15;
        } else if (scale.equalsIgnoreCase("re")) {
            cTemp = temperature * 4/5;
        } else if (scale.equalsIgnoreCase("Ra")) {
            cTemp = (temperature - 491.67) * 5/9;
        }
        
        return cTemp;
    }
    public static double convertToKelvin(String scale, int temperature) {
        double kTemp = 0;
        
        if(scale.equalsIgnoreCase("f")) {
            kTemp = (temperature + 459.67) * 5/9;
        } else if (scale.equalsIgnoreCase("c")) {
            kTemp = temperature + 273.15;
        } else if (scale.equalsIgnoreCase("re")) {
            kTemp = (temperature / .8) + 273.15;
        } else if (scale.equalsIgnoreCase("Ra")) {
            kTemp = temperature * 5/9;
        }
        
        return kTemp;
    }
    public static double convertToReaumur(String scale, int temperature) {
        double reTemp = 0;
        
        if(scale.equalsIgnoreCase("f")) {
            reTemp = (temperature - 32) * .44444;
        } else if (scale.equalsIgnoreCase("c")) {
            reTemp = temperature * 5/4;
        } else if (scale.equalsIgnoreCase("k")) {
            reTemp = (temperature - 273.15) * .8;
        } else if (scale.equalsIgnoreCase("Ra")) {
            reTemp = (temperature - 491.67) * 4/9;
        }
        
        return reTemp;
    }
    public static double convertToRankine(String scale, int temperature) {
        double raTemp = 0;
        
        if(scale.equalsIgnoreCase("f")) {
            raTemp = temperature + 459.67;
        } else if (scale.equalsIgnoreCase("c")) {
            raTemp = (temperature + 273.15) * 9/5;
        } else if (scale.equalsIgnoreCase("k")) {
            raTemp = temperature * 9/5;
        } else if (scale.equalsIgnoreCase("re")) {
            raTemp = temperature * 9/4 + 491.67;
        }
        
        return raTemp;
    }
}
