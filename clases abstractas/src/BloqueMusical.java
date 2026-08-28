public class BloqueMusical implements ActivablePorRedstone {

     @Override
    public void activar() {System.out.println("Bloque musical se activa y emite un sonido");}
    @Override
    public void desactivar() {System.out.println("Bloque musical recibe señal y deja de reproducir.");}

}
