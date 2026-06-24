# Plan: UI/UX de mi-app-gym

## Contexto
App Gradio en `008/002 - PRA/008 - vision_artificial_aplicada/mi-app-gym/` desplegada en HuggingFace Space `manuelcpv92/mi-app-gym`. Usa MediaPipe Pose Heavy. Ya se aplicó rediseño UI y fix de formato de imagen.

## Decisiones tomadas
- **Ubicación**: mantener `mi-app-gym/` en su ruta actual. No mover.
- **Bug fix**: normalizar imagen a RGB uint8 antes de MediaPipe (elimina error "model does not support image input").
- **Rediseño base**: tema oscuro premium, acento `#c8ff00`, layout 2 columnas, badges, score numérico en métricas.
- **Límite visual**: evitar glow animado continuo para no forzar repaints.

## Pendiente por decidir
- **Borde neón**: aplicar solo en botón primario y badge OK con `box-shadow` reducido y hover discreto, o descartar neón y mantener bordes planos.

## Pasos si se aprueba neón
1. Agregar `box-shadow` en `.gr-button-primary` y `.coach-badge.ok`.
2. Probar en HF Space (spinner, feedback, carga).

## Validación
- `git push` a HF Space y verificar que arranque sin error de Gradio.
- Subir imagen y confirmar detección + métricas.
- Revisar que no haya parpadeo del glow en mobile.
