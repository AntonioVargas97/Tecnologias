public class Main {
    public static void main(String[] args) throws Exception {
        
        Piston miPiston = new Piston();
        Lampara miLampara = new Lampara();
        Puerta miPuerta = new Puerta();
        BloqueMusical miBloque = new BloqueMusical();
        
        System.out.println("Se activó la palanca");
        miPiston.activar();
        miPuerta.activar();
        miLampara.activar();
        miBloque.activar();
        

        System.out.println("Se desactivó la palanca");
        miPiston.desactivar();
        miPuerta.desactivar();
        miLampara.desactivar();
        miBloque.desactivar();

        Zombie miZombie = new Zombie();
        Esqueleto miEsqueleto = new Esqueleto();


        miZombie.quemarEnLava();
        miEsqueleto.quemarEnLava();
        
        miZombie.atacar();
        miEsqueleto.atacar();

    }


}
