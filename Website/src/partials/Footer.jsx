import React from 'react';
import { Link } from 'react-router-dom';

function Footer() {
  return (
    <footer>
      <div className="max-w-6xl mx-auto px-4 sm:px-6">

        {/* Top area: Blocks */}
        <div className="grid sm:grid-cols-12 gap-8 py-8 md:py-12 border-t border-gray-200">

          {/* 1st block */}
          <div className="sm:col-span-12 lg:col-span-3">
            <div className="mb-2">
              {/* Logo */}
              <Link to="/" className="inline-block" aria-label="DeepGenX">
              <div className="flex-shrink-0 mr-4">
            {/* Logo */}
        
            <img className="h-20 w-auto" src="https://cdn.discordapp.com/attachments/939536871262912546/939944565404729344/Screen_Shot_2022-02-06_at_1.04.02_PM.png" alt="Workflow" />
          </div>
              </Link>
            </div>
          </div>
          </div>
      </div>
    </footer>
  );
}

export default Footer;