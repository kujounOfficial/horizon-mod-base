// Hook helper: native_settings_click
fn on_client_tick_post(game: &mut crate::game::Game<'_>) {
    crate::game::horizonmod_glue::on_client_tick_post(game);
}