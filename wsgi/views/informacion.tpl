% include('header.tpl')
			<!-- Banner -->
			<section id="banner">
				<div class="content">
					<span class="image"><img src="/static/images/pic01.jpg" alt=""/></span>
				</div>
				<a href="#one" class="goto-next scrolly">Next</a>
			</section>


			<section id="one" class="wrapper special fade">
				<div class="container">
					<header>
						<h2>Obtenga informaci&oacute;n r&aacute;pidamente sobre sus artistas, grupos o &aacute;lbums favoritos.</h2>
						<p>Rellene el siguiente formulario y pulse el bot&oacute;n buscar para mostrar la informaci&oacute;n que desee.</p>
					</header>
					<form method="post" action="#">
						<div class="row uniform 50%">
							<div class="select-wrapper">
								<select name="category" id="category">
									<option value="">Seleccione el tipo de búsqueda</option>
									<option value="1">Grupo</option>
									<option value="2">Artista</option>
									<option value="3">&Aacute;lbum</option>
								</select>
							</div>
							<div class="6u 12u$(xsmall)">
								<input type="text" name="name" id="name" value="" placeholder="Escriba aquí lo que quiere buscar" />
							</div>
							<div>
								<input type="submit" value="Buscar" class="fit special" />
							</div>
						</div>
					</form>
				</div>
			</section>
% include('footer.tpl')
