% include('header.tpl')
			<!-- Banner -->
			<section id="banner">
				<div class="content">
					<header>
						<h2>{{titulo}}</h2>
						<ul class="actions">
							<li><a href="#one" class="button special">Mu&eacute;strame la informaci&oacuten</a></li>
						</ul>
					</header>
					<span class="image"><img src={{imagen}} alt=""/></span>
				</div>
				<a href="#one" class="goto-next scrolly">Next</a>
			</section>
			<section id="one">
				<p><span class="image left"><img src={{imagen}} alt=""></span><h2>{{titulo}}</h2>{{texto}}</p>
			</section>

% include('footer.tpl')
