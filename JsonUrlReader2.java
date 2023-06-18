/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.apache.beam.examples;

import com.fasterxml.jackson.core.exc.StreamReadException;
import com.fasterxml.jackson.databind.DatabindException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.beam.examples.Aire;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;

/**
 *
 * @author Alan
 */
public class JsonUrlReader2 {
    
    public JsonUrlReader2(){
        
    }
    
    
    public ArrayList<Locales> cargarURL ()throws StreamReadException,DatabindException,MalformedURLException,IOException{
        String url = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php/";
        
        ArrayList<Locales> aLocales = new ArrayList();
        
        ObjectMapper mapper = new ObjectMapper();
        
        System.out.println("Inicando mapper en JsonUrlReader");
        JsonNode node = mapper.readTree(new URL(url));

        System.out.println("Finalizando mapper en JsonUrlReader");
        
        Iterator<JsonNode> it = node.iterator();
        
        Locales a = null;
        
        a = new Locales();
        a.setFecha("Fecha");
        a.setLocal_id("Id");
        a.setFk_region("Fk_region");
        a.setFk_comuna("Fk_comuna");
        a.setFk_localidad("Fk_localidad");
        a.setLocal_nombre("Local_nombre");
        a.setComuna_nombre("Comuna_nombre");
        a.setLocalidad_nombre("Localidad_nombre");
        a.setLocal_direccion("local_direccion");
        a.setFuncionamiento_hora_apertura("Funcionamiento_hora_apertura");
        a.setFuncionamiento_hora_cierre("Funcionamiento_hora_cierre");
        a.setLocal_telefono("Local_telefono");
        a.setLocal_lat("Local_lat");
        a.setLocal_lng("Local_lgn");
        a.setFuncionamiento_dia("Funcionamiento_dia");
        
        aLocales.add(a);
        
        int i = 1;
        
        while (it.hasNext()){
            JsonNode n = it.Next();
            
            JsonNode r = n.get("realtime");
            
            Iterator<JsonNode> itRealtime = r.iterator();
            while (itRealtime.hasNext()){
                a = new Locales();
                
                a.setFecha(n.get("fecha").asText());
                a.setLocal_id(String.valueOf(i));
                a.setFk_region(n.get("fk_region").asText());
                a.setFk_comuna(n.get("fk_comuna").asText());
                a.setFk_localidad(n.get("fk_localidad").asText());
                a.setLocal_nombre(n.get("local_nombre").asText());
                a.setComuna_nombre(n.get("comuna_nombre").asText());
                a.setLocalidad_nombre(n.get("localidad_nombre").asText());
                a.setLocal_direccion(n.get("local_direccion").asText());
                a.setFuncionamiento_hora_apertura(n.get("funcionamiento_hora_apertura").asText());
                a.setFuncionamiento_hora_cierre(n.get("funcionamiento_hora_cierre").asText());
                a.setLocal_telefono(n.get("local_telefono").asText());
                a.setLocal_lat(n.get("local_lat").asText());
                a.setLocal_lng(n.get("local_lng").asText());
                a.setFuncionamiento_dia(n.get("funcionamiento_dia").asText());
                
                JsonNode nRealtime = itRealtime.Next();
            }//while itRealtime
        }
        return aLocales;
        
        
    
        
        
        
        
    } 
    
}//jsonUrlReader
